import pymysql
import datetime
from datetime import datetime, timedelta

class Input_data:
    def __init__(self, name, sex, birthday, number_borrowed, user_delayed, blacklist, publisher, writer, genre_id, book_name, published_year, bought_date, books_borrowed):
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.number_borrowed = number_borrowed
        self.user_delayed = user_delayed
        self.blacklist = blacklist
        self.publisher = publisher
        self.writer = writer
        self.genre_id = genre_id
        self.book_name = book_name
        self.published_year = published_year
        self.bought_date = bought_date
        self.books_borrowed = books_borrowed

    #유저 추가
    def add_user(self):
        name = input("이름을 입력하시오: ")
        sex = int(input("성별을 선택하세요: 1.남자 2.여자: "))
        if sex == 1:
            sex_value = 'M'
        else:
            sex_value = 'F'
        birthday = input("생일을 입력하세요 예시 1992-11-25: ")
        number_borrowed = 0
        user_delayed = 'N'
        blacklist = 'N'

        conn = pymysql.connect(
            host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
            db='library_assignment', charset='utf8', use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO User (name, sex, birthday, number_borrowed, user_delayed, blacklist) VALUES (%s, %s, %s, %s, %s, %s)",
                       (name, sex_value, birthday, number_borrowed, user_delayed, blacklist))
        conn.commit()
        conn.close()

    #책 추가
    def add_book(self):
        publisher = input("출판사 이름을 입력하세요: ")
        writer = input("저자의 이름을 입력하세요: ")
        genre_id = input("책의 장르를 입력하세요 100:경제, 200:소설, 300:인문, 400:추리, 500:요리, 600:만화, 700:아동: ")
        genre_id = int(genre_id)
        if genre_id not in [100, 200, 300, 400, 500, 600, 700]:
            print("유효하지 않은 장르입니다.")
            return
        book_name = input("책 이름을 입력하세요: ")
        published_year = input("출판 연도를 입력하세요: 예시) 2025: ")
        bought_date = input("구입 날짜를 입력하세요 예시) 2025-02-15: ")
        books_borrowed = 'N'

        conn = pymysql.connect(
            host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
            db='library_assignment', charset='utf8', use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Books (publisher, writer, genre_id, book_name, published_year, bought_date, books_borrowed) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (publisher, writer, genre_id, book_name, published_year, bought_date, books_borrowed))
        conn.commit()
        conn.close()

class Output_data(Input_data):
    def __init__(self, name, sex, birthday, number_borrowed, user_delayed, blacklist, publisher, writer, genre_id, book_name, published_year, bought_date, books_borrowed):
        super().__init__(name, sex, birthday, number_borrowed, user_delayed, blacklist, publisher, writer, genre_id, book_name, published_year, bought_date, books_borrowed)

    #모든 유저 확인
    def all_user(self):
        conn = pymysql.connect(
            host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
            db='library_assignment', charset='utf8')
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User")
        rows1 = cursor.fetchall()
        for row in rows1:
            print(f"ID: {row[0]}, 이름: {row[1]}, 성별: {row[2]}, 생일: {row[3]}, 대출 수: {row[4]}, 연체: {row[5]}, 블랙리스트: {row[6]}")
        conn.close()

    #유저 한명 확인
    def one_user(self):
        conn = pymysql.connect(
            host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
            db='library_assignment', charset='utf8')
        find = input("이름을 입력하시오: ")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User WHERE name = %s", (find,))
        rows1 = cursor.fetchall()
        if rows1:
            for row in rows1:
                print(f"ID: {row[0]}, 이름: {row[1]}, 성별: {row[2]}, 생일: {row[3]}, 대출 수: {row[4]}, 연체: {row[5]}, 블랙리스트: {row[6]}")
        else:
            print('존재하지 않는 이름입니다.')
        conn.close()

    #모든 책 확인
    def all_books(self):
        conn = pymysql.connect(
            host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
            db='library_assignment', charset='utf8')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books")
        rows1 = cursor.fetchall()
        for row in rows1:
            print(f"ID: {row[0]}, 출판사: {row[1]}, 저자: {row[2]}, 장르: {row[3]}, 책 이름: {row[4]}, 출판 연도: {row[5]}, 구입 날짜: {row[6]}, 대출 여부: {row[7]}")
        print("총 책 수:", len(rows1))
        conn.close()

    #책 하나 확인
    def one_books(self):
        conn = pymysql.connect(
            host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
            db='library_assignment', charset='utf8')
        find = input("책 이름 또는 저자 또는 장르(100:경제, 200:소설, 300:인문, 400:추리, 500:요리, 600:만화, 700:아동)을 입력하시오: ")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books WHERE book_name = %s OR writer = %s OR genre_id = %s", (find, find, find))
        rows1 = cursor.fetchall()
        if rows1:
            for row in rows1:
                print(f"ID: {row[0]}, 출판사: {row[1]}, 저자: {row[2]}, 장르: {row[3]}, 책 이름: {row[4]}, 출판 연도: {row[5]}, 구입 날짜: {row[6]}, 대출 여부: {row[7]}")
        else:
            print('존재하지 않는 책입니다.')
        print("총 책 수:", len(rows1))
        conn.close()

    #유저 수정
    def update_user(self):
        conn = pymysql.connect(
        host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
        db='library_assignment', charset='utf8')
        try:
            with conn.cursor() as cur:
                find = input("수정할 유저의 id를 입력하세요: ")  
                cur.execute("SELECT * FROM User WHERE user_id = %s", (find,))
                row2 = cur.fetchone()
                if not row2:
                    print(f"'{find}' 유저를 찾을 수 없습니다.")
                    return
                num = int(input("수정 (1.이름, 2.성별, 3.생일: "))

                if num == 1:
                    new_name = input("수정할 이름을 입력하세요: ")
                    cur.callproc('user_update_name', (find, new_name))
                elif num == 2:
                    new_sex = input("수정할 성별을 선택하세요: 1.남자 2.여자: ")
                    if new_sex == '1':
                        new_sex = 'M'
                    else:
                        new_sex = 'F'
                    cur.callproc('user_update_sex', (find, new_sex))
                elif num == 3:
                    new_birthday = input("수정할 생일을 입력하세요 예시 1992-11-25: ")
                    cur.callproc('user_update_birthday', (find, new_birthday))
                else:
                    print("잘못된 입력입니다.")
                    return
                print("수정 완료")
                conn.commit()

        except Exception as e:
            print(f"데이터베이스 작업 중 오류가 발생했습니다: {e}")
            conn.rollback()  
        conn.close()


    #책 수정
    def update_book(self):
        conn = pymysql.connect(
        host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
        db='library_assignment', charset='utf8', use_unicode=True,
        cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as cur:
                find = input("수정할 책의 ID를 입력하세요: ")
                cur.execute("SELECT * FROM Books WHERE book_id = %s", (find,))
                row2 = cur.fetchone()
                if not row2:
                    print(f"'{find}' 책을 찾을 수 없습니다.")
                    return
                num = int(input("수정 (1.출판사, 2.저자, 3.장르, 4.책 이름, 5.출판 연도, 6.구입일자): "))

                if num == 1:
                    new_publisher = input("수정할 출판사 이름을 입력하세요: ") 
                    cur.callproc('book_update_publisher', (find, new_publisher))  
                elif num == 2:
                    new_writer = input("수정할 저자 이름을 입력하세요: ") 
                    cur.callproc('book_update_writer', (find, new_writer))  
                elif num == 3:
                    genre_id = int(input("수정할 책의 장르를 입력하세요 100:경제, 200:소설, 300:인문, 400:추리, 500:요리, 600:만화, 700:아동: "))
                    cur.callproc('gene_update_gene', (find, genre_id))  
                elif num == 4:
                    new_book_name = input("수정할 책 이름을 입력하세요: ")  
                    cur.callproc('book_update_book_name', (find, new_book_name))  
                elif num == 5:
                    new_published_year = input("수정할 출판 연도를 입력하세요: 예시) 2025: ")  
                    cur.callproc('book_update_published_year', (find, new_published_year)) 
                elif num == 6:
                    new_bought_date = input("수정할 구입 날짜를 입력하세요 예시) 2025-02-15: ")
                    cur.callproc('book_update_bought_date', (find, new_bought_date))  
                else:
                    print("잘못된 입력입니다.")
                    return
                print("수정 완료")
                conn.commit()

        except Exception as e:
            print(f"데이터베이스 작업 중 오류가 발생했습니다: {e}")
            conn.rollback()
        conn.close()

    #유저 삭제
    def delete_user(self):
        conn = pymysql.connect(
            host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
            db='library_assignment', charset='utf8', use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor)
        num1 = int(input("삭제할 유저의 번호를 입력하세요: "))
        with conn.cursor() as cur:
            cur.callproc('user_delete', (num1,))
            if cur.rowcount == 0:
                print(f"'{num1}'번 유저를 찾을 수 없습니다.")
            else:
                conn.commit()
                print(f"'{num1}'번 유저의 정보가 성공적으로 삭제되었습니다.")
        conn.close()

    #책 삭제
    def delete_book(self):
        conn = pymysql.connect(
            host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
            db='library_assignment', charset='utf8', use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor)
        num2 = int(input("삭제할 책의 번호를 입력하세요: "))
        with conn.cursor() as cur:
            cur.callproc('book_delete', (num2,))
            if cur.rowcount == 0:
                print(f"'{num2}'번 책을 찾을 수 없습니다.")
            else:
                conn.commit()
                print(f"'{num2}'번 책의 정보가 성공적으로 삭제되었습니다.")
        conn.close()

#실패 일주일 후에 반납 안할시는 연체자가 되고 5회 이상시 블랙리스트가 되는것 실패
    #Borrow_Log에 있는 borrowed가 'Y' 일 때 책이 빌려지고 일주일 뒤에 user DB에 있는 user_delayed와  Delayed DB에 있는 times 를 1씩 증가시키는 함수
    # def delayed_book(self):
    #     conn = pymysql.connect(
    #         host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
    #         db='library_assignment', charset='utf8', use_unicode=True,
    #         cursorclass=pymysql.cursors.DictCursor)
    #     cursor = conn.cursor()
    #     # 수정: Users 테이블 사용, return_date IS NULL 추가, 날짜 비교 명확화
    #     cursor.execute("""
    #         SELECT b.user_id, b.borrowed, b.borrow_delayed, b.borrowed_date, d.times 
    #         FROM Borrow_Log b 
    #         INNER JOIN Delayed d ON b.user_id = d.user_id 
    #         WHERE b.borrowed = 'Y' 
    #         AND b.borrow_delayed = 'N' 
    #         AND b.return_date IS NULL 
    #         AND b.borrowed_date <= %s
    #     """, (datetime.now() - timedelta(days=7),))
    #     rows1 = cursor.fetchall()
    #     if rows1:
    #         for row in rows1:
    #             user_id = row['user_id']
    #             cursor.execute("""
    #                 UPDATE Borrow_Log 
    #                 SET borrow_delayed = 'Y' 
    #                 WHERE user_id = %s 
    #                 AND borrowed = 'Y' 
    #                 AND return_date IS NULL 
    #                 AND borrowed_date <= %s
    #             """, (user_id, datetime.now() - timedelta(days=7)))
    #             cursor.execute("UPDATE Delayed SET times = times + 1 WHERE user_id = %s", (user_id,))
    #             cursor.execute("UPDATE Users SET user_delayed = 'Y' WHERE user_id = %s", (user_id,))
    #         conn.commit()
    #         print("연체된 대출 기록이 업데이트되었습니다.")
    #     else:
    #         print("연체된 대출 기록이 없습니다.")
    #     conn.close()


    # 연체자 및 블랙리스트 확인
    def bad_user(self):
        conn = pymysql.connect(
            host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
            db='library_assignment', charset='utf8', use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor)
        find = input("이름을 입력하시오: (연체자 확인은 a, 블랙리스트 확인은 b) ")
        cursor = conn.cursor()
        if find == 'a':
            cursor.execute("SELECT * FROM User WHERE user_delayed = 'Y'")
            rows1 = cursor.fetchall()
            if rows1:
                print('연체자 목록')
                for row in rows1:
                    print(f"ID: {row['user_id']}, 이름: {row['name']}, 성별: {row['sex']}, 생일: {row['birthday']}, 대출 수: {row['number_borrowed']}, 연체: {row['user_delayed']}, 블랙리스트: {row['blacklist']}")
            else:
                print("연체자 목록이 없습니다.")
        elif find == 'b':
            cursor.execute("SELECT * FROM User WHERE blacklist = 'Y'")
            rows1 = cursor.fetchall()
            if rows1:
                print("블랙리스트 사용자 목록:")
                for row in rows1:
                    print(f"ID: {row['user_id']}, 이름: {row['name']}, 성별: {row['sex']}, 생일: {row['birthday']}, 대출 수: {row['number_borrowed']}, 연체: {row['user_delayed']}, 블랙리스트: {row['blacklist']}")
            else:
                print("블랙리스트에 등록된 사용자가 없습니다.")
        else:
            cursor.execute("SELECT * FROM User WHERE name = %s", (find,))
            rows1 = cursor.fetchall()
            if rows1:
                for row in rows1:
                    print(f"ID: {row['user_id']}, 이름: {row['name']}, 성별: {row['sex']}, 생일: {row['birthday']}, 대출 수: {row['number_borrowed']}, 연체: {row['user_delayed']}, 블랙리스트: {row['blacklist']}")
            else:
                print("존재하지 않는 이름입니다.")
        conn.close()

    #특정 유저 대출 현황 조회
    def specific(self):
        conn = pymysql.connect(
            host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
            db='library_assignment', charset='utf8', use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor)
        find = input("유저 id를 입력하시오: ")
        cursor = conn.cursor()
        cursor.execute("""SELECT u.name, u.number_borrowed, u.user_delayed, u.blacklist, b.borrowed_date, c.book_id, c.book_name, c.publisher, c.writer FROM Borrow_Log b INNER JOIN User u ON b.user_id = u.user_id INNER JOIN Books c ON b.book_id = c.book_id WHERE u.user_id = %s""", (find,))
        rows1 = cursor.fetchall()
        if rows1:
            for row in rows1:
                print(f"이름: {row['name']}, 빌린 횟수: {row['number_borrowed']}, 연체 유무: {row['user_delayed']}, 블랙리스트 유무: {row['blacklist']}, 책 빌린 날짜: {row['borrowed_date']}, 책 번호: {row['book_id']}, 책 이름: {row['book_name']}, 출판사: {row['publisher']}, 저자: {row['writer']}")
        else:
            print('존재하지 않은 유저입니다.')
        conn.close()

    #모든 빌린 책 확인
    def allrentbook(self):
        conn = pymysql.connect(
            host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
            db='library_assignment', charset='utf8', use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        sql_query = """
            SELECT
                Borrow_Log.borrowed_date,
                User.name,
                Books.book_name,
                Borrow_Log.return_date
            FROM
                Borrow_Log
            INNER JOIN
                User ON Borrow_Log.user_id = User.user_id
            INNER JOIN
                Books ON Borrow_Log.book_id = Books.book_id;
        """
        cursor.execute(sql_query)
        borrowed_details = cursor.fetchall()
        print("전체 대출 목록: ")
        for detail in borrowed_details:
            if detail['return_date'] is not None:
                pass 
            else:
                print(f"대출 날짜: {detail['borrowed_date']}, 유저 이름: {detail['name']}, 책 이름: {detail['book_name']}")
        conn.close()

    #책 빌리기
    def book_rent(self):
        conn = pymysql.connect(
            host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
            db='library_assignment', charset='utf8', use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        name = input("대출 진행자의 유저의 id를 입력하시오: ")
        cursor.execute("SELECT user_id, blacklist FROM User WHERE user_id = %s", (name,))
        user = cursor.fetchone()
        if not user:
            print("존재하지 않는 유저입니다.")
            conn.close()
            return
        if user['blacklist'] == 'Y':
            print("블랙리스트 유저는 대출할 수 없습니다.")
            conn.close()
            return
        book_id = int(input("대출할 책의 번호를 입력하세요: "))
        cursor.execute("SELECT book_id, books_borrowed FROM Books WHERE book_id = %s", (book_id,))
        book = cursor.fetchone()
        if not book:
            print("존재하지 않는 책입니다.")
            conn.close()
            return
        if book['books_borrowed'] == 'Y':
            print("이미 대출 중인 책입니다.")
            conn.close()
            return
        date = input("대출 날짜 입력('2025-08-11' 형식에 맞춰 입력): ")

        cursor.execute("INSERT INTO Borrow_Log (book_id, user_id, borrowed_date, borrowed, borrow_delayed) VALUES (%s, %s, %s, %s, %s)",
                      (book_id, user['user_id'], date, 'Y', 'N'))
        cursor.execute("UPDATE Books SET books_borrowed = 'Y' WHERE book_id = %s", (book_id,))
        cursor.execute("UPDATE User SET number_borrowed = number_borrowed + 1 WHERE user_id = %s", (user['user_id'],))
        conn.commit()
        print("대출이 완료되었습니다.")
        conn.close()

    #책 반납
    def book_return(self):
        conn = pymysql.connect(
            host='34.171.242.249', port=3306, user='acorm', password='acorm1234',
            db='library_assignment', charset='utf8', use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        name = input("반납할 유저의 ID를 입력하시오: ")
        cursor.execute("SELECT user_id FROM User WHERE user_id = %s", (name,))
        user = cursor.fetchone()
        if not user:
            print("존재하지 않는 유저입니다.")
            conn.close()
            return
        book_id = int(input("반납할 책의 번호를 입력하세요: "))
        cursor.execute("SELECT book_id FROM Books WHERE book_id = %s", (book_id,))
        book = cursor.fetchone()
        if not book:
            print("존재하지 않는 책입니다.")
            conn.close()
            return
        cursor.execute("SELECT borrowed FROM Borrow_Log WHERE user_id = %s AND book_id = %s AND borrowed = 'Y'", (user['user_id'], book_id))
        borrow = cursor.fetchone()
        if not borrow:
            print("해당 유저가 이 책을 대출하지 않았습니다.")
            conn.close()
            return
        date = input("반납 날짜 입력('2025-08-11' 형식에 맞춰 입력): ")
        cursor.execute("UPDATE Borrow_Log SET return_date = %s, borrowed = 'N' WHERE user_id = %s AND book_id = %s",
                      (date, user['user_id'], book_id))
        cursor.execute("UPDATE Books SET books_borrowed = 'N' WHERE book_id = %s", (book_id,))
        conn.commit()
        print("반납이 완료되었습니다.")
        conn.close()

class Menu(Input_data):
    def __init__(self, name, sex, birthday, number_borrowed, user_delayed, blacklist, publisher, writer, genre_id, book_name, published_year, bought_date, books_borrowed):
        super().__init__(name, sex, birthday, number_borrowed, user_delayed, blacklist, publisher, writer, genre_id, book_name, published_year, bought_date, books_borrowed)
        self.output = Output_data(name, sex, birthday, number_borrowed, user_delayed, blacklist, publisher, writer, genre_id, book_name, published_year, bought_date, books_borrowed)

    def main_menu(self):
        while True:
            print("=========$국립 도서관 시스템$========")
            print("1. 사용자 관리 ")
            print("2. 도서 관리 ")
            print("3. 대출 관리 ")
            print("9. 종료")
            print("=====================================")
            choice = int(input("메뉴를 선택하세요: "))
            if choice == 1:
                self.user_menu()
            elif choice == 2:
                self.book_menu()
            elif choice == 3:
                self.borrow_menu()
            elif choice == 9:
                print("프로그램을 종료합니다.")
                break
            else:
                print("!! 메뉴에 없는 번호입니다. 다시 입력해주세요.")

    def user_menu(self):
        while True:
            print("=============$유저 메뉴$=============")
            print("  1. 유저 추가")
            print("  2. 모든 유저 검색")
            print("  3. 특정 유저 검색")
            print("  4. 유저 정보 수정")
            print("  5. 유저 삭제")
            print("  9. 이전 메뉴로")
            print("=====================================")
            try:
                choice = int(input("유저 메뉴를 선택하세요: "))
            except ValueError:
                print("!! 숫자를 입력해주세요.")
                continue
            if choice == 1:
                self.add_user()
                print("유저가 추가되었습니다.")
            elif choice == 2:
                self.output.all_user()
            elif choice == 3:
                self.output.one_user()
            elif choice == 4:
                self.output.update_user()
            elif choice == 5:
                self.output.delete_user()
            elif choice == 9:
                print("메인 메뉴로 돌아갑니다.")
                break
            else:
                print("!! 메뉴에 없는 번호입니다. 다시 입력해주세요.")

    def book_menu(self):
        while True:
            print("=============$도서 메뉴$=============")
            print("1. 도서 추가")
            print("2. 모든 도서 검색 ")
            print("3. 도서 검색 ")
            print("4. 도서 수정 ")
            print("5. 도서 삭제 ")
            print("9. 이전 메뉴로")
            print("=====================================")
            try:
                choice = int(input("도서 메뉴를 선택하세요: "))
            except ValueError:
                print("!! 숫자를 입력해주세요.")
                continue
            if choice == 1:
                self.add_book()
                print("도서가 추가되었습니다.")
            elif choice == 2:
                self.output.all_books()
            elif choice == 3:
                self.output.one_books()
            elif choice == 4:
                self.output.update_book()
            elif choice == 5:
                self.output.delete_book()
            elif choice == 9:
                print("메인 메뉴로 돌아갑니다.")
                break
            else:
                print("!! 메뉴에 없는 번호입니다. 다시 입력해주세요.")

    def borrow_menu(self):
        while True:
            print("=============$대출 메뉴$=============")
            print("1. 특정 유저 대출 현황 조회")
            print("2. 전체 대출 목록 조회")
            print("3. 연체자 목록 및 블랙리스트 조회")
            print("4. 도서 대출")
            print("5. 도서 반납")
            print("9. 이전 메뉴로")
            print("=====================================")
            try:
                choice = int(input("대출 메뉴를 선택하세요: "))
            except ValueError:
                print("!! 숫자를 입력해주세요.")
                continue
            if choice == 1:
                self.output.specific()
            elif choice == 2:
                self.output.allrentbook()
            elif choice == 3:
                self.output.bad_user()
            elif choice == 4:
                self.output.book_rent()
            elif choice == 5:
                self.output.book_return()
            elif choice == 9:
                print("메인 메뉴로 돌아갑니다.")
                break
            else:
                print("!! 메뉴에 없는 번호입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    menu = Menu(None, None, None, 0, 'N', 'N', None, None, None, None, None, None, 'N')
    menu.main_menu()
