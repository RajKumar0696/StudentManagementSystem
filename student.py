# create student class
from student_class import StudentClass
class Student:
    student_dictionary = {}
    school_name='Goudie'

    def __init__(self):
        self.roll_no = input("\n\t Enter the student roll number:")
        self.name = input("\t Enter the student name:")
        self.phone_number = input("\t Enter the student phone number:")
        self.address = input("\t Enter the student address:")
        classNumber = input("\t Enter the student class number:")

        if classNumber in StudentClass.classes:
            StudentClass.classes[classNumber].studentList.append(self)
        else:
            new_class = StudentClass(classNumber)
            new_class.studentList.append(self)
            # StudentClass.classes[classNumber] = new_class

        self.student_class = StudentClass.classes[classNumber]

        print("\nStudent Added Successfully")
        self.getStudent()

    def getStudent(self):
        print("\n---STUDENT DETAILS---\n")
        print("\tRoll Number  : ", self.roll_no)
        print("\tName         : ", self.name)
        print("\tPhone Number : ", self.phone_number)
        print("\tAddress      : ", self.address)
        print("\tClass        : ", self.student_class.classNumber)
        print("\tSchool Name : ", Student.school_name)

    def updateStudent(self):
        print("\t\tselect option to update student details")
        print("\t\t\t1)To change student name")
        print("\t\t\t2)To change student phone number")
        print("\t\t\t3)To change student address")
        print("\t\t\t4)To change student class")
        option = input("\t\tEnter any above given option:")
        print()

        if option in ['1', '2', '3', '4']:
            if option == '1':
                self.name = input("\t\t\tEnter the student new name:")
                print("\n\t\tStudent name changed successfully")
            elif option == '2':
                self.phone_number = input("\t\t\tEnter the student new phone number:")
                print("\n\t\tStudent phone number changed successfully")
            elif option == '3':
                self.address = input("\t\t\tEnter the student new address:")
                print("\n\t\tStudent address changed successfully")
            elif option == '4':
                new_class = input("\t\t\tEnter the student new class name:")
                self.student_class.studentList.remove(self)
                try:
                    self.student_class = StudentClass.classes[new_class]
                    self.student_class.studentList.append(self)
                except:
                    addClass = StudentClass(new_class)
                    self.student_class = addClass
                    addClass.studentList.append(self)
                print("\n\t\tStudent class changed successfully")
            self.getStudent()
        else:
            print("\n\t\t\tYou have choosen wrong option")

    @classmethod
    def updateSchoolName(cls, new_school_name):
        cls.school_name = new_school_name

    @classmethod
    def getTotalStudentCount(cls):
        return len(cls.student_dictionary)
