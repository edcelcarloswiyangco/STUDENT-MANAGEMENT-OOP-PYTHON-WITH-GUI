from db_config import connect_db

class EnrollmentManagement:
    def __init__(self):
        self.db = connect_db()

    def enroll_student(self, student_id, course_id):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO enrollments (student_id,course_id) VALUES (%s,%s)",(student_id,course_id))
        self.db.commit()#
        print("Student enrolled in course successfully.")

    def list_enrollments(self):
        cursor = self.db.cursor()#
        cursor.execute("""
        SELECT students.name, courses.course_name 
        FROM enrollments
        JOIN students ON enrollments.student_id = students.id
        JOIN courses ON enrollments.course_id = courses.id
        """)
        for enrollment in cursor.fetchall():
            print(enrollment)