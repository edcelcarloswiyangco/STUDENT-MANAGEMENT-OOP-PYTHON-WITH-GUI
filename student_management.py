from db_config import connect_db

class StudentManagement:
    def __init__(self):
        self.db = connect_db()

    def add_student(self,name,email,age):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO students (name,email,age) VALUES (%s,%s,%s)",(name,email,age))
        self.db.commit()#
        print("Student added successfully")

    def edit_student(self, student_id, name = None, email = None, age = None):
        cursor = self.db.cursor()
        update_fields = []
        values = []
        if name:
            update_fields.append("name = %s")
            values.append(name)
        if email:
            update_fields.append("email = %s")
            values.append(email)
        if age:
            update_fields.append("age = %s")
            values.append(age)
        values.append(student_id)
        cursor.execute(f"UPDATE students SET {', '.join(update_fields)} WHERE id = %s",values)#
        self.db.commit()#
        print("Student updated successfully")

    def delete_student(self,student_id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s",(student_id,))
        print("Student deleted successfully")

    def list_student(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM students")
        for student in cursor.fetchall():
            print(student)