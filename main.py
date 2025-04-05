from user_management import UserManagement
from student_management import StudentManagement
from course_management import CourseManagement
from enrollment_management import EnrollmentManagement#
import getpass

def main():
    usermgmt = UserManagement()
    studmgnt = StudentManagement()
    coursemgmt = CourseManagement()
    enrollmgmt = EnrollmentManagement()

    while True:
        print("\n-- Welcom to the Studednt Management System --")
        print("1. Register")
        print("2. Login")
        choice = input("Enter your choice(1-2):")
        
        if choice == "1":
            username = input("Enter a username:")
            password = getpass.getpass("Enter new password:")
            usermgmt.register_user(username, password)#
        elif choice == "2":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password:")#
            if usermgmt.login_user(username,password):#
                print("Login successful")
                while True:
                    print("Student Management System")
                    print("1. Add Student")
                    print("2. Edit Student")
                    print("3. Delete Student")
                    print("4. List Students")
                    print("5. Add Course")
                    print("6. Edit Course")
                    print("7. Delete Course")
                    print("8. List Courses")
                    print("9. Enroll Student in Course")
                    print("10. List enrollment")
                    print("11. Exit")
                    choice = input("Enter a choice (1-11):")#
                    if choice == "1":
                        name = input("Enter Student name:")
                        email = input("Enter student email:")
                        age = input("Enter student age:")
                        studmgnt.add_student(name,email,age)
                    elif choice == "2":
                        student_id = input("Enter studnet ID to edit:")
                        name = input("Enter new name(or press enter to skip):")
                        email = input("Enter new email(or press enter to skip):")
                        age = input("Enter new age(or press enter to skip):")
                        studmgnt.edit_student(student_id,name,email,age)
                    elif choice == "3":
                        student_id = input("Enter student id to delete:")
                        studmgnt.delete_student(student_id)#
                    elif choice == "4":
                        studmgnt.list_student()
                    elif choice == "5":
                        name = input("Enter course name:")
                        description = input("Enter course description:")
                        coursemgmt.add_course(name,description)#
                    elif choice == "6":
                        course_id = input("Enter course ID to edit: ")
                        name = input("Enter new name desription(or press enter to skip):")#
                        description = input("Enter new course description(or press enter to skip):")
                        coursemgmt.edit_course(course_id,name,description)
                    elif choice == "7":
                        course_id = input("Enter course ID to delete:")
                        coursemgmt.delete_course(course_id)
                    elif choice == "8":
                        coursemgmt.list_course()
                    elif choice == "9":
                        student_id = input("Enter student ID:")
                        course_id = input("Enter course ID:")
                        enrollmgmt.enroll_student(student_id,course_id)
                    elif choice == "10":
                        enrollmgmt.list_enrollments()#
                    elif choice == "11":
                        print("Exiting the system.")
                        break
                    else:#
                        print("Invalid choice please try again.")
            else:
                print("Invalid username or password")  
        else:
            print("Invalid Choice please try again")

main()