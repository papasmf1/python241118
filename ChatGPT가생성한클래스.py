# Person 클래스: 기본 클래스 (Base Class)
class Person:
    # 생성자: id와 name을 초기화
    def __init__(self, id, name):
        self.id = id  # ID를 저장
        self.name = name  # 이름을 저장

    # printInfo 메서드: 객체 정보를 문자열로 반환
    def printInfo(self):
        return f"ID: {self.id}, Name: {self.name}"

# Manager 클래스: Person 클래스를 상속받음
class Manager(Person):
    # 생성자: id, name 외에 title 변수를 추가
    def __init__(self, id, name, title):
        super().__init__(id, name)  # 부모 클래스(Person)의 생성자를 호출
        self.title = title  # Manager 고유의 title 정보를 저장

    # printInfo 메서드: title 정보를 포함하도록 오버라이드
    def printInfo(self):
        return f"ID: {self.id}, Name: {self.name}, Title: {self.title}"

# Employee 클래스: Person 클래스를 상속받음
class Employee(Person):
    # 생성자: id, name 외에 skill 변수를 추가
    def __init__(self, id, name, skill):
        super().__init__(id, name)  # 부모 클래스(Person)의 생성자를 호출
        self.skill = skill  # Employee 고유의 skill 정보를 저장

    # printInfo 메서드: skill 정보를 포함하도록 오버라이드
    def printInfo(self):
        return f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}"

# 메인 실행 블록
if __name__ == "__main__":
    # Person 클래스 테스트
    p1 = Person(1, "Alice")  # ID 1, 이름 Alice
    p2 = Person(2, "Bob")  # ID 2, 이름 Bob
    print(p1.printInfo())  # 예상 출력: "ID: 1, Name: Alice"
    print(p2.printInfo())  # 예상 출력: "ID: 2, Name: Bob"

    # Manager 클래스 테스트
    m1 = Manager(3, "Charlie", "Team Lead")  # ID 3, 이름 Charlie, 직책 Team Lead
    m2 = Manager(4, "Dana", "Project Manager")  # ID 4, 이름 Dana, 직책 Project Manager
    print(m1.printInfo())  # 예상 출력: "ID: 3, Name: Charlie, Title: Team Lead"
    print(m2.printInfo())  # 예상 출력: "ID: 4, Name: Dana, Title: Project Manager"

    # Employee 클래스 테스트
    e1 = Employee(5, "Eve", "Python")  # ID 5, 이름 Eve, 기술 Python
    e2 = Employee(6, "Frank", "JavaScript")  # ID 6, 이름 Frank, 기술 JavaScript
    print(e1.printInfo())  # 예상 출력: "ID: 5, Name: Eve, Skill: Python"
    print(e2.printInfo())  # 예상 출력: "ID: 6, Name: Frank, Skill: JavaScript"

    # 다양한 Person, Manager, Employee 객체를 테스트
    # 각 클래스에서 생성된 객체들을 리스트에 추가
    people = [
        p1,  # Person 객체
        p2,  # Person 객체
        m1,  # Manager 객체
        m2,  # Manager 객체
        e1,  # Employee 객체
        e2,  # Employee 객체
        Manager(7, "Grace", "CTO"),  # Manager 객체, ID 7, 이름 Grace, 직책 CTO
        Employee(8, "Hank", "DevOps"),  # Employee 객체, ID 8, 이름 Hank, 기술 DevOps
        Person(9, "Ivy"),  # Person 객체, ID 9, 이름 Ivy
        Employee(10, "Jack", "Machine Learning")  # Employee 객체, ID 10, 이름 Jack, 기술 Machine Learning
    ]

    # 리스트에 있는 모든 객체에 대해 printInfo 호출
    for person in people:
        print(person.printInfo())
