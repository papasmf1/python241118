import sqlite3
import random

class ElectronicsDatabase:
    """
    SQLite를 사용하여 전자제품 데이터를 관리하는 클래스.

    기능:
    - 데이터베이스 초기화 및 테이블 생성
    - 전자제품 데이터 삽입, 수정, 삭제, 조회
    """
    def __init__(self, db_name="electronics.db"):
        """
        클래스 초기화 메서드. 데이터베이스 연결 및 테이블 초기화.

        :param db_name: 데이터베이스 파일 이름 (기본값: 'electronics.db')
        """
        self.connection = sqlite3.connect(db_name)  # 데이터베이스 연결
        self.cursor = self.connection.cursor()      # SQL 쿼리를 실행하기 위한 커서 생성
        self.create_table()                         # 테이블 생성 메서드 호출

    def create_table(self):
        """
        전자제품 데이터를 저장할 테이블을 생성하는 메서드.
        테이블 이름: electronics
        컬럼:
        - id: 제품 ID (기본 키)
        - name: 제품명
        - price: 가격
        """
        query = """
        CREATE TABLE IF NOT EXISTS electronics (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
        self.cursor.execute(query)  # 테이블 생성 SQL 쿼리 실행
        self.connection.commit()    # 변경 사항 커밋

    def insert_product(self, product_id, name, price):
        """
        새로운 전자제품 데이터를 삽입하는 메서드.

        :param product_id: 제품 ID
        :param name: 제품명
        :param price: 가격
        """
        query = "INSERT INTO electronics (id, name, price) VALUES (?, ?, ?)"
        self.cursor.execute(query, (product_id, name, price))  # 데이터 삽입
        self.connection.commit()                              # 변경 사항 커밋

    def update_product(self, product_id, name=None, price=None):
        """
        기존 전자제품 데이터를 수정하는 메서드.

        :param product_id: 수정할 제품의 ID
        :param name: 변경할 제품명 (기본값: None)
        :param price: 변경할 가격 (기본값: None)
        """
        if name:
            # 제품명을 수정하는 쿼리
            query = "UPDATE electronics SET name = ? WHERE id = ?"
            self.cursor.execute(query, (name, product_id))
        if price:
            # 제품 가격을 수정하는 쿼리
            query = "UPDATE electronics SET price = ? WHERE id = ?"
            self.cursor.execute(query, (price, product_id))
        self.connection.commit()  # 변경 사항 커밋

    def delete_product(self, product_id):
        """
        전자제품 데이터를 삭제하는 메서드.

        :param product_id: 삭제할 제품의 ID
        """
        query = "DELETE FROM electronics WHERE id = ?"
        self.cursor.execute(query, (product_id,))  # 데이터 삭제
        self.connection.commit()  # 변경 사항 커밋

    def select_all_products(self):
        """
        테이블에 저장된 모든 전자제품 데이터를 조회하는 메서드.

        :return: 모든 전자제품 데이터 리스트 (튜플 형태)
        """
        query = "SELECT * FROM electronics"
        self.cursor.execute(query)  # 모든 데이터 조회 쿼리 실행
        return self.cursor.fetchall()  # 조회된 결과 반환

    def select_product_by_id(self, product_id):
        """
        특정 ID의 전자제품 데이터를 조회하는 메서드.

        :param product_id: 조회할 제품의 ID
        :return: 해당 제품 데이터 (튜플 형태) 또는 None
        """
        query = "SELECT * FROM electronics WHERE id = ?"
        self.cursor.execute(query, (product_id,))  # 특정 ID의 데이터 조회
        return self.cursor.fetchone()  # 조회된 결과 반환

    def close(self):
        """
        데이터베이스 연결을 종료하는 메서드.
        """
        self.connection.close()  # 데이터베이스 연결 종료


# 샘플 데이터 생성
def generate_sample_data(db, num_samples=100):
    """
    샘플 데이터를 생성하여 데이터베이스에 삽입하는 함수.

    :param db: ElectronicsDatabase 클래스 객체
    :param num_samples: 생성할 샘플 데이터 개수 (기본값: 100)
    """
    # 샘플 제품 이름 목록
    product_names = [
        "Smartphone", "Laptop", "Tablet", "Smartwatch", "Desktop PC",
        "Gaming Console", "Bluetooth Speaker", "Wireless Earbuds",
        "Smart TV", "Digital Camera", "Monitor", "Keyboard",
        "Mouse", "Router", "External Hard Drive", "Printer",
        "Scanner", "Projector", "Drone", "VR Headset"
    ]

    for i in range(1, num_samples + 1):
        # 랜덤한 제품 이름 및 가격 생성
        name = random.choice(product_names)
        price = round(random.uniform(50, 2000), 2)
        # 생성된 데이터 삽입
        db.insert_product(i, f"{name} {i}", price)


# 실행 예제
if __name__ == "__main__":
    # 데이터베이스 객체 생성
    db = ElectronicsDatabase()

    # 샘플 데이터 삽입
    generate_sample_data(db)

    # 모든 제품 출력
    print("All Products:")
    for product in db.select_all_products():
        print(product)

    # 특정 제품 업데이트
    print("\nUpdating Product with ID 1...")
    db.update_product(1, name="Updated Smartphone", price=899.99)

    # 특정 제품 확인
    print("\nProduct with ID 1:")
    print(db.select_product_by_id(1))

    # 제품 삭제
    print("\nDeleting Product with ID 2...")
    db.delete_product(2)

    # 모든 제품 출력
    print("\nAll Products After Deletion:")
    for product in db.select_all_products():
        print(product)

    # 데이터베이스 연결 종료
    db.close()
