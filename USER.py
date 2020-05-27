import sqlite3
import check
from Db import DBConnection
# from ADMIN import Admin
# from EMPLOYEE import Employee

class User:
        def start(self):
            """
            It takes input accordingly redirects the code flow to the Admin or Employee 
            :return: True/False
            """
            try:
                print("****** WELCOME TO CAB SERVICE ******")
                ch = input("\n\nEnter\n1.Admin\n2.Employee\n3.Exit")
                if ch == '1':
                        email = input("Enter email")
                        password = input("Enter password")
                        if check.check_email(email) == False:
                            print("******Invalid Email******")
                            return False
                        admin_obj = Admin(email, password)
                        if admin_obj.check():
                            return True
                        else:
                            return False

                elif ch == '2':
                        email = input("Enter email")
                        password = input("Enter password")
                        if check.check_email(email) == False:
                            print("******Invalid Email******")
                            return False
                        con = DBConnection().sql_connection()
                        cursorObj = con.cursor()
                        emp_id = cursorObj.execute("SELECT Id from Employee where email ='{}' AND password = '{}'".format(email, password)).fetchone()
                        emp_obj = Employee(email, password, emp_id)
                        if emp_obj.check():
                            return True
                        else:
                            return False
                        
                elif ch == '3':
                        return False
                
                else:
                        print ("Invalid input")
                        return False

            except IOError as e:
                print(e)
                return False

# print(os.getcwd())
user_obj = User()
user_obj.start()
