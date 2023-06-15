class Person:
    def sayHi(self):
        print('안녕')


class Student(Person):
    def study(self):
        print('공부')


daniel = Student()
daniel.sayHi()
daniel.study()
