from db_config import connect_db
import hashlib


def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()


class UserManagement:
    def __init__(self):
        self.db = connect_db()#

    def register_user(self,username,password,role='user'):
         cursor = self.db.cursor()
         hashed_password = hash_password(password)
         cursor.execute("INSERT INTO users (username,password,role) VALUES (%s,%s,%s)",(username,hashed_password,role))#
         self.db.commit()
         print("User registered successfully")

    def login_user(self,username,password):
         cursor = self.db.cursor()
         hashed_password = hash_password(password)
         cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",(username,hashed_password))
         user = cursor.fetchone()
         if user:
              print(f"Welcome, {username}")
              return user
         else:
              print("Invalid username or password")
              return None