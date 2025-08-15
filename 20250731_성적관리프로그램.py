all_stud = []

class OnePerson:
  def __init__(self, name, kor, eng, math):
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math

class ScoreManager:
  def __init__(self, op: OnePerson):
    self.op = op
    self.total = op.kor + op.eng + op.math
    self.avg = self.total / 3
    self.rank = self._calculate_grade(self.avg)

    all_stud.append([op.name, op.kor, op.eng, op.math, self.total, self.avg, self.rank])

  def _calculate_grade(self, avg):
    if avg >= 90:
      return "A"
    elif avg >= 80:
      return "B"
    elif avg >= 70:
      return "C"
    elif avg >= 60:
      return "D"
    else:
      return "F"

  def calculate_ranks(self):
    all_stud.sort(key=lambda x: x[5], reverse=True)
    for i in range(len(all_stud)):
      if len(all_stud[i]) > 7:
        all_stud[i].pop(-1)
      all_stud[i].append(i + 1)

  def print_all(self):
    self.calculate_ranks()
    for student in all_stud:
      print(f"이름: {student[0]}, 국어: {student[1]}, 영어: {student[2]}, 수학: {student[3]}, 총점: {student[4]}, 평균: {round(student[5], 2)}, 학점: {student[6]}, 등수: {student[7]}")

  def delete_student(self, name):
    for i in range(len(all_stud)):
      if all_stud[i][0] == name:
        all_stud.pop(i)
        print(f"'{name}' 학생을 삭제했습니다.") 
        return
    print("학생을 찾을 수 없습니다.")

  def modify_student(self, name):
    for student in all_stud:
      if student[0] == name:
        num = int(input("수정할 분야 선택하세요(0.이름 1.국어 2.영어 3.수학)(0~3): "))
        if num == 0:
          student[0] = input("수정할 이름 입력: ")
        elif num == 1:
          student[1] = int(input("수정할 국어 점수 입력: "))
        elif num == 2:
          student[2] = int(input("수정할 영어 점수 입력: "))
        elif num == 3:
          student[3] = int(input("수정할 수학 점수 입력: "))
        else:
          print("잘못된 입력입니다.")
          return
        student[4] = student[1] + student[2] + student[3]
        student[5] = round(student[4] / 3, 2)
        student[6] = self._calculate_grade(student[5])
        print("성공적으로 수정되었습니다.")
        return
    print("해당 학생을 찾을 수 없습니다.")

  def print_one(self, name):
    for student in all_stud:
      if student[0] == name:
        print(f"이름: {student[0]}, 국어: {student[1]}, 영어: {student[2]}, 수학: {student[3]}, 총점: {student[4]}, 평균: {round(student[5], 2)}, 학점: {student[6]}, 등수: {student[7] if len(student) > 7 else '미계산'}")
        return
    print("해당 학생이 존재하지 않습니다.")

class Menu:
  def __init__(self):
    self.manager = None  # 아직 객체 없음

  def run(self):
    while True:
      print("===== 성적 관리 시스템 =====")
      print("1. 성적 입력")
      print("2. 등수 계산")
      print("3. 전체 성적 출력")
      print("4. 개인 성적 출력")
      print("5. 성적 수정")
      print("6. 성적 삭제")
      print("7. 종료")
      print("★성적 입력/수정/삭제 후 반드시 '2. 등수 계산'을 실행해주세요~!★")
      print("===========================")
      choice = input("메뉴 선택: ")

      if choice == "1":
        name = input("이름: ")
        kor = int(input("국어 점수: "))
        eng = int(input("영어 점수: "))
        math = int(input("수학 점수: "))
        person = OnePerson(name, kor, eng, math) # OnePerson 클래스에 성적 입력
        self.manager = ScoreManager(person) # 성적 입력후 인스턴스

      elif choice == "2":
        if self.manager:
          self.manager.calculate_ranks()
          print("등수 계산 완료!")
        else:
          print("성적이 입력되지 않았습니다.")

      elif choice == "3":
        if self.manager:
          self.manager.print_all()
        else:
          print("성적이 입력되지 않았습니다.")

      elif choice == "4":
        if self.manager:
          name = input("성적 열람할 학생 이름 입력: ")
          self.manager.print_one(name)
        else:
          print("성적이 입력되지 않았습니다.")

      elif choice == "5":
        if self.manager:
          name = input("수정할 학생 이름: ")
          self.manager.modify_student(name)
        else:
          print("성적이 입력되지 않았습니다.")

      elif choice == "6":
        if self.manager:
          name = input("삭제할 학생 이름: ")
          self.manager.delete_student(name)
        else:
          print("성적이 입력되지 않았습니다.")

      elif choice == "7":
        print("프로그램을 종료합니다.")
        break
      else:
        print("잘못된 입력입니다.")

if __name__ == "__main__": ## 메인 메뉴 실행 코드
  menu = Menu()
  menu.run()
