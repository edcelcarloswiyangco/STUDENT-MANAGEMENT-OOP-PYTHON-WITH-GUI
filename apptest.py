import tkinter as tk
from tkinter import messagebox
from db_config import connect_db
from user_management import UserManagement
from student_management import StudentManagement
from course_management import CourseManagement
from enrollment_management import EnrollmentManagement


class StudentManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.user_mgmt = UserManagement()
        self.create_login_page()

    def create_login_page(self):
        tk.Label(self.root, text="Username").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Password").grid(row=1, column=0, padx=10, pady=10)

        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Login", command=self.login_user).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Register", command=self.register_user).grid(row=3, column=0, columnspan=2, pady=10)

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.user_mgmt.login_user(username, password)
        if user:
            self.root.destroy()
            self.create_main_system_window()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = "user"  # Default role
        self.user_mgmt.register_user(username, password, role)
        messagebox.showinfo("Success", "Registration successful")

    def create_main_system_window(self):
        main_window = tk.Tk()
        main_window.title("Student Management System")

        functions = [
            ("Add Student", self.add_student_window),
            ("Edit Student", self.edit_student_window),
            ("Delete Student", self.delete_student_window),
            ("List Students", self.list_students_window),
            ("Add Course", self.add_course_window),
            ("Edit Course", self.edit_course_window),
            ("Delete Course", self.delete_course_window),
            ("List Courses", self.list_courses_window),
            ("Enroll Student", self.enroll_student_window),
            ("List Enrollments", self.list_enrollments_window),
            ("Exit", main_window.quit),
        ]

        for i, (text, command) in enumerate(functions):
            tk.Button(main_window, text=text, command=command).grid(row=i, column=0, padx=10, pady=5, sticky="w")

        main_window.mainloop()

    # Define individual function windows
    def add_student_window(self):
        self.open_form_window("Add Student", StudentManagement().add_student, ["name", "email", "age"])

    def edit_student_window(self):
        self.open_form_window("Edit Student", StudentManagement().edit_student, ["student_id", "new_name", "new_email", "new_age"])

    def delete_student_window(self):
        self.open_form_window("Delete Student", StudentManagement().delete_student, ["student_id"])

    def list_students_window(self):
        self.show_list_window("List Students", StudentManagement().list_student)

    def add_course_window(self):
        self.open_form_window("Add Course", CourseManagement().add_course, ["course_name", "course_description"])

    def edit_course_window(self):
        self.open_form_window("Edit Course", CourseManagement().edit_course, ["course_id", "new_name", "new_description"])

    def delete_course_window(self):
        self.open_form_window("Delete Course", CourseManagement().delete_course, ["course_id"])

    def list_courses_window(self):
        self.show_list_window("List Courses", CourseManagement().list_course)

    def enroll_student_window(self):
        self.open_form_window("Enroll Student", EnrollmentManagement().enroll_student, ["student_id", "course_id"])

    def list_enrollments_window(self):
        self.show_list_window("List Enrollments", EnrollmentManagement().list_enrollments)

    def open_form_window(self, title, action, fields):
        form_window = tk.Toplevel()
        form_window.title(title)

        tk.Label(form_window, text="Enter Details").grid(row=0, column=0, columnspan=2, pady=10)
        inputs = []

        def submit_action():
            values = [entry.get() for entry in inputs]
            try:
                action(*values)  # Call the function passed with the values from the form
                messagebox.showinfo("Success", f"{title} completed successfully!")
                form_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        # Add form fields dynamically based on the fields list
        for i, field in enumerate(fields):
            tk.Label(form_window, text=field.capitalize()).grid(row=i + 1, column=0, padx=10, pady=5)
            entry = tk.Entry(form_window)
            entry.grid(row=i + 1, column=1, padx=10, pady=5)
            inputs.append(entry)

        tk.Button(form_window, text="Submit", command=submit_action).grid(row=len(fields) + 1, column=0, columnspan=2, pady=10)

    def show_list_window(self, title, data_function):
        list_window = tk.Toplevel()
        list_window.title(title)

        data = data_function()  # Get the data from the relevant function
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                tk.Label(list_window, text=value).grid(row=i, column=j, padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementGUI(root)
    root.mainloop()
