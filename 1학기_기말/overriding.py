class Person:
    def sayHi(self):
        print('안녕하세요.')


class Student(Person):
    def sayHi(self):
        print('반갑습니다.')


daniel = Student()
daniel.sayHi()
