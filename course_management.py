from db_config import connect_db

class CourseManagement:#
    def __init__(self):
        self.db = connect_db()

    def add_course(self, name, description):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO courses (course_name, description) VALUES (%s, %s)",(name,description))#
        self.db.commit()#
        print("Course added successfully")

    def edit_course(self, course_id, name = None, description = None):
        cursor = self.db.cursor()#
        update_fields = []
        values = []
        if name:
            update_fields.append("course_name = %s")#
            values.append(name)#
        if description:
            update_fields.append("description = %s")
            values.append(description)#
        values.append(course_id)#
        cursor.execute(f"UPDATE courses SET {', '.join(update_fields)} WHERE id = %s",values)
        self.db.commit()
        print("Course updated successfully.")

    def delete_course(self, course_id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM courses WHERE id = %s",(course_id,))#
        print("Course deleted successfully.")
    
    def list_course(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM courses")
        for course in cursor.fetchall():
            print(course)