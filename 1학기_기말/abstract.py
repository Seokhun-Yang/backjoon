from abc import *


class MiddleSchoolStudent(metaclass=ABCMeta):
    @abstractmethod
    def factorization(self):
        pass

    @abstractmethod
    def drawingGraph(self):
        pass


class HighSchoolStudent(MiddleSchoolStudent):
    def factorization(self):
        print('인수 분해')

    def drawingGraph(self):
        print('그래프 그리기')


daniel = HighSchoolStudent()
daniel.factorization()
daniel.drawingGraph()
