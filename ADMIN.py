import sqlite3
from datetime import datetime
import check
from Db import DBConnection
import itertools

class Admin:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def check(self):
        """
        Checks whether the input Id and password is in the admin table
        :return: True/False
        """
        con = DBConnection().sql_connection()
        cursorObj = con.cursor()
        user = cursorObj.execute("SELECT * from Admin where Email ='{}' AND Password = '{}'".format(self.email, self.password)).fetchone()
        # print(type(user))
        if not user:
            print("Admin with Email ='{}' AND Password = '{}' not found. Kindly recheck your email id or password".format(self.email, self.password))
            return False
        print("Welcome Admin {}".format(user[3]))
        return (self.options())


    def options(self):
        """
        Gives the admin a list of options.
        :return: True/False
        """
        op = input("1.Add Employee\n2.Update Employee\n3.Delete Employee\n4.Add Cab"
              "\n5.Update Cab\n6.Delete Cab\n")
        if op == '1':
            if self.addEmp():
                return True
            else:
                return False
        elif op =='2':
            if self.updateEmp():
                return True
            else:
                return False
        elif op == '3':
            if self.deleteEmp():
                return True
            else:
                return False
        elif op == '4':
            if self.addCab():
                return True
            else:
                return False
        elif op == '5':
            if self.updateCab():
                return True
            else:
                return False
        elif op == '6':
            if self.deleteCab():
                return True
            else:
                return False
        else:
            print("Invalid Input")
            return False

    def addEmp(self):
        """
        Creates Employees
        :return: True/False
        """
        try:
            con = DBConnection().sql_connection()
            cursor_obj = con.cursor()
            name = input("Enter name")
            if check.check_name(name) == False:
                print("Invalid Name - Can only have alphabets")
                return False
            email = input("Enter email")
            if check.check_email(email) != True:
                print("Invalid email id")
                return False
            password = input("Enter password")
            sqlite_insert_user_query = """INSERT INTO Employee (name, email, password, createdAT, updatedAt) 
                                                   VALUES ('{}','{}','{}','{}','{}')""".format(name, email, password,datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), datetime.today().strftime('%Y-%m-%d-%H:%M:%S') )
            cursor_obj.execute(sqlite_insert_user_query)
            con.commit()
            cursor_obj.close()
            print("Created")
            return True
        except IOError as e:
            print(e)
            return False

    def updateEmp(self):
        """
        Updates The employee
        :return: True/False
        """
        try:
            con = DBConnection().sql_connection()
            cursor_obj = con.cursor()
            emp_id = input("Enter Employee ID to be updated")
            emp = cursor_obj.execute("SELECT * from Employee WHERE Id ='{}' ".format(emp_id)).fetchone()
            if not emp:
                print("*** Entered Employee Id does not exist***")
                return False
            print("Press Enter If You Do Not Wish To Update")
            name = input("name:{} ".format(emp[3]))
            if name != "":
                sql_user_update_query = """Update Employee set name = '{}', updatedAt ='{}' where Id = '{}'""".format(name, datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), emp_id)
                cursor_obj.execute(sql_user_update_query)
            password = input("password:{} ".format(emp[2]))
            if password != "":
                sql_update_query = """Update Employee set role = '{}',updatedAt = '{}' where Id = '{}'""".format(password,datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), emp_id)
                cursor_obj.execute(sql_update_query)
            con.commit()
            cursor_obj.close()
            return True
        except IOError as e:
            print(e)
            return False

    def addCab(self):
        """
        Creates A supervising team
        :return: True/False
        """
        try:
            con = DBConnection().sql_connection()
            cursor_obj = con.cursor()
            cab_no = input("Enter Cab number plate ")
            route_no = input("Enter the route no for to be assigned to the cab")
            route= cursor_obj.execute("SELECT * from routes where route_no ='{}'".format(route_no)).fetchone()
            # print(type(route))
            if not route:
                print(
                    "Route - '{}' not found. Kindly recheck your route id".format(route_no))
                return False
            timing = input("Enter timing for the cab in %H:%M:%S format")
            seats = input("Enter number of seats in the cab")

            sqlite_insert_user_query = """INSERT INTO Cab (cab_no, route_no, timing,seats,createdAt, updatedAt)
                                                   VALUES ('{}','{}','{}','{}','{}','{}')""".format(cab_no, route_no, timing, seats, datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
            cursor_obj.execute(sqlite_insert_user_query)
            con.commit()
            cursor_obj.close()
            return True
        # print("Created")
        except sqlite3.Error as e:
            print(e)
            return False

    def deleteEmp(self): ###TEST BOOKING CANCEL ONE- Employee dependecies####
        """
        Deletes employees
        :return: True/False
        """
        try:
            con = DBConnection().sql_connection()
            cursor_obj = con.cursor()
            emp_id = input("Enter employee id to be deleted")
            if check.check_id(emp_id) == False:
                print("Invalid Employee Id")
                return False
            sql_delete_emp_query = """Delete from Employee where Id = '{}'""".format(emp_id)
            cursor_obj.execute(sql_delete_emp_query)
            sql_delete_booking_query = """Delete from bookings where emp_id = '{}'""".format(emp_id)
            cursor_obj.execute(sql_delete_booking_query)
            con.commit()
            cursor_obj.clodeleteEmpse()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def deleteCab(self):
        """
        Deletes Supervising team

        :return: True/False
        """

        try:
            con = DBConnection().sql_connection()
            cursor_obj = con.cursor()
            cab_id = input("Enter Cab Id to be deleted")
            if check.check_id(cab_id) == False:
                print("Invalid Cab Id")
                return False
            sql_del_query = """Delete from Cab where Id = '{}'""".format(cab_id)
            cursor_obj.execute(sql_del_query)
            sql_del_query = """Delete from bookings where cab_id = '{}'""".format(cab_id)
            cursor_obj.execute(sql_del_query)
            con.commit()
            cursor_obj.close()
            return True
        except sqlite3.Error as e:
            print(e)
            return False


    def updateCab(self):
        """
        updates the supervising team
        :return: True/False
        """
        try:
            con = DBConnection().sql_connection()
            cursor_obj = con.cursor()
            cab_id = input("Enter Cab ID to be updated")
            query = cursor_obj.execute("SELECT * from Cab WHERE Id ='{}' ".format(cab_id)).fetchone()
            if query == None:
                print("***Entered Cab Id does not exist***")
                return False
            print("Press Enter If You Do Not Wish To Update")
            seats = input("Seats:{} ".format(query[1]))
            if seats != "":
                    sql_user_update_query = """Update Cab set seats = '{}', updatedAt ='{}' where Id = '{}'""".format(
                        seats, datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), cab_id)
                    cursor_obj.execute(sql_user_update_query)
            route_no = input("Enter route number you wish to update:{} ".format(query[5]))
            route = cursor_obj.execute("SELECT * from routes where route_no ='{}'".format(route_no)).fetchone()
            # print(type(route))
            if not route:
                print(
                    "Route - '{}' not found. Kindly recheck your route id".format(route_no))
                return False
            if route_no != "":
                sql_user_update_query = """Update Cab set route_no = '{}' where Id = '{}'""".format(route_no,cab_id)
                cursor_obj.execute(sql_user_update_query)
            cursor_obj.close()
            con.commit()
            cursor_obj.close()
            return True
        except IOError as e:
            print(e)
            return False



admin = Admin('aastha@gmail.com','123')
admin.updateCab()
# admin.addCab()