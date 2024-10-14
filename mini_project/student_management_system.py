class Student:
    student_Dictionary = {}
    school_name = "Sreenidhi Institute"

    def __init__(self):
        self.roll_no = input("\nEnter the student roll Number: ")
        self.name = input("\nEnter the student name: ")
        self.phone_number = input("\nEnter the student phone number: ")
        self.address = input("\nEnter the student address: ")
        student_class = input("Enter the student class [EX:1,2,3,4,5,6,7,8]: ")

        if student_class in StudentClass.classes:
            StudentClass.classes[student_class].studentList.append(self)
        else:
            new_class = StudentClass(student_class)
            new_class.studentList.append(self)
            StudentClass.classes[student_class] = new_class

        self.student_class = StudentClass.classes[student_class]
        print("\nStudent details added successfully!!!")
        self.getStudent()

    def getStudent(self):
        print("\n--Student Details--\n")
        print("\tRoll number:", self.roll_no)
        print("\tName:", self.name)
        print("\tPhone Number:", self.phone_number)
        print("\tAddress:", self.address)
        print("\tClass:", self.student_class.name)
        print("\tSchool Name:", Student.school_name)

    def updateStudent(self):
        print("\t\tSelect option to update student details\n")
        print("\t\t\t1) To change student Name")
        print("\t\t\t2) To change student phone number")
        print("\t\t\t3) To change student Address")
        print("\t\t\t4) To change student class\n")
        option = input("\t\tEnter any above given options: ")

        if option in ['1', '2', '3', '4']:
            if option == '1':
                self.name = input("\t\t\tEnter the student New Name: ")
                print("\n\t\tStudent Name Changed Successfully")
            elif option == '2':
                self.phone_number = input("\t\t\tEnter the student New Phone Number: ")
                print("\n\t\tStudent Phone Number Changed Successfully")
            elif option == '3':
                self.address = input("\t\t\tEnter the student New Address: ")
                print("\n\t\tStudent Address Changed Successfully")
            elif option == '4':
                new_class = input("\t\t\tEnter the student New Class: ")
                self.student_class.studentList.remove(self)
                if new_class in StudentClass.classes:
                    self.student_class = StudentClass.classes[new_class]
                    self.student_class.studentList.append(self)
                else:
                    add_class = StudentClass(new_class)
                    self.student_class = add_class
                    add_class.studentList.append(self)
                print("\t\t\tStudent Class Changed Successfully\n")
        else:
            print("\n\t\t\tYou have chosen a wrong option")

    @classmethod
    def updateSchoolName(cls, new_school_name):
        cls.school_name = new_school_name

    @classmethod
    def getTotalStudentCount(cls):
        return len(cls.student_Dictionary)


class StudentClass:
    classes = {}

    def __init__(self, name):
        self.name = name
        StudentClass.classes[name] = self
        self.studentList = []


def main():
    print("--Welcome to Sreenidhi Institute of Science and Technology---\n")
    print("\t1) To get student details")
    print("\t2) To add new student details")
    print("\t3) To remove student details")
    print("\t4) To update student details")
    print("\t5) To update school name")
    print("\t6) To get the number of students in school")
    print("\t7) To get all student details")

    option = input("Enter any given option: ")

    if option == '1':
        roll_no = input("\tEnter the Roll number of the student: ")
        try:
            Student.student_Dictionary[roll_no].getStudent()
        except KeyError:
            print("\t\tStudent Not Found or entered wrong roll number")
    elif option == '2':
        new_student = Student()
        Student.student_Dictionary[new_student.roll_no] = new_student
    elif option == '3':
        roll_no = input("\tEnter the Roll number of the student: ")
        try:
            student = Student.student_Dictionary.pop(roll_no)
            student.student_class.studentList.remove(student)
            print("\t\t***", roll_no, "*** student details removed successfully")
        except KeyError:
            print("\t\tNo student to delete")
    elif option == '4':
        roll_no = input("\tEnter the Roll number of the student: ")
        try:
            Student.student_Dictionary[roll_no].updateStudent()
        except KeyError:
            print("\n\t\tYou have entered the wrong Roll number")
    elif option == '5':
        new_school_name = input("\tEnter the New School Name: ")
        Student.updateSchoolName(new_school_name)
        print("\nSchool Name Changed Successfully")
    elif option == '6':
        print("Total Number of Students in the School:", Student.getTotalStudentCount())
    elif option == '7':
        if Student.student_Dictionary:
            print("Total Number of Students in the School:", Student.getTotalStudentCount())
            print("\nTotal Student List with Details\n")
            for sNo, student in enumerate(Student.student_Dictionary.values()):
                print(f"Student-{sNo + 1}")
                student.getStudent()
                print()
        else:
            print("\tNo students available")


if __name__ == "__main__":
    option = "Yes"
    while option.lower() == "yes":
        main()
        option = input("\n\t\t\tDo you want to continue [Yes/No]? ").capitalize()
