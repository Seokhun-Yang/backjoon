class Person:
    def sayHi(self):
        print('안녕')


class Student:
    def study(self):
        print('공부')


class Citizen(Person, Student):
    def vote(self):
        print('투표')


daniel = Citizen()
daniel.sayHi()
daniel.study()
daniel.vote()
