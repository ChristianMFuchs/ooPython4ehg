#
class human():

    def __init__(self, _firstName: str, _secondName: str, _age: int):
        self.firstName = _firstName
        self.secondName = _secondName
        self.age = _age

    def getAge(self):
        return self.age
    
    def getFirstNAme(self):
        return self.firstName
    
    def getSecondName(self):
        return self.secondName
    
    def setAge(self, neweAge: int):
        return self.age
    

class pupil(human):

    def __init__(self, _firstName: str, _secondName: str, _age: int):
        super().__init__(self, _firstName, _secondName, _age)
     
        self.averageGrade = 0

    def getAverageMark(self):
        return self.averageGrade
    
    def setAverageGrade(self, _newAverageGrade: int):
        self.averageGrade = _newAverageGrade

class teacher(human):

    def __init__(self, _firstName: str, _secondName: str, _age: int):
        super().__init__(self, _firstName, _secondName, _age)
     
        self.numberOfCourses = 0

    def getNumberOfCourses(self):
        return self.numberOfCourses
    
    def setNumberOfCourses(self, _newNumberOfCourses: int):
        self.numberOfCourses = _newNumberOfCourses