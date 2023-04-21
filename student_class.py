class StudentClass:
    classes = {}

    # constructor
    def __init__(self, classNumber):
        self.classNumber = classNumber
        self.studentList = []
        StudentClass.classes[classNumber] = self


