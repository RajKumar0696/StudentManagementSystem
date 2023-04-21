from student_class import StudentClass
from student import Student

# create menu
def main():
    print("\n***********  Welcome To Goudie School  ***********")
    print("\t1) To Get Student Details")
    print("\t2) To Add New Student")
    print("\t3) To Remove Student")
    print("\t4) To Update Student Details")
    print("\t5) To Update School Name")
    print("\t6) To Get Number Of Student In School")
    print("\t7) To Get All Student Details")
    print("\t8) To Get Any Class Student Details")

    option = int(input("Enter any above given option:"))

    if option == 1:
        roll_no = input("\tEnter the Roll Number of a Student:")
        try:
            Student.student_dictionary[roll_no].getStudent()
        except:
            print("\tYou Have EnterThe Wrong Roll Number")

    elif option == 2:
        new_student = Student()
        Student.student_dictionary[new_student.roll_no] = new_student

    elif option == 3:
        roll_no = input("\tEnter the Roll Number of a Student:")
        canDelete = input("\t\tAre you sure to delete [y/n?]")

        if canDelete == 'y':

            try:
                student = Student.student_dictionary.pop(roll_no)
                student.student_class.studentList.remove(student)

                print("\t\tRoll Number", roll_no, "Student deleted successfully")

            except:
                print("\t\tNo student there to delete")



    elif option == 4:
        roll_no = input("\tEnter the Roll Number of a Student:")
        print()
        try:
            Student.student_dictionary[roll_no].updateStudent()
        except:
            print("\n\t\tYou have enter the wrong roll number")

    elif option == 5:
        new_school_name = input("\tEnter the new school name:")
        Student.updateSchoolName(new_school_name)
        print("School name changed successfully")

    elif option == 6:
        print("Total number of students in school:", Student.getTotalStudentCount())

    elif option == 7:
        if Student.student_dictionary:
            print("Total number of students in school:", Student.getTotalStudentCount())
            print("\n Total student list with details\n")
            for sNo, student in enumerate(Student.student_dictionary.values()):
                print("Student-", sNo + 1)
                student.getStudent()
                print()
        else:
            print("\tNo student there")

    elif option == 8:
        try:
            classRoom = StudentClass.classes[input("\tEnter the class name:")]
            print("\tStudents of class-", classRoom.classNumber)
            print(f"\nTotal number of students in class{classRoom.classNumber}:{len(classRoom.studentList)}")
            print()
            for sNo, student in enumerate(classRoom.studentList):
                print("Student-", sNo + 1)
                student.getStudent()
                print()
        except:
            print("\nYou entered wrong class name or no student there")


if __name__ == '__main__':
    choice = 'y'
    while choice == 'y':
        main()
        choice = input("\nDo You Want To Continue[y/n?]:")
        print()
