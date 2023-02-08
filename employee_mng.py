import random
import time

class Admin:
    emp_id = 102
    def __init__(self):
        self.dict1 = {101:[101,"sai","sai78","developer",30000,7028998786,"sai78@gmail.com"],102:[102,"pankaj","pankaj78","developer",60000,9987868584,"pankaj78@gmail.com"]}
        self.attendance2 = {101:10,102:10}

    def add_emp(self):
        print("\n     ------->>    Add New Employee    <<-------         \n")
        self.emp_id += 1

        """if employee id already exist then takes new id"""
        if self.emp_id in self.dict1:
            self.emp_id += 100
        
        username = input("Enter employee's username:    ")
        password = input("Enter employee's password:    ")
        job_role = input("Enter employee's job role:    ")
        try:
            salary = int(input("Enter employee's salary  :    "))
        except:
            print("\nOops!! Invalid Input ....\nEnter Salary Only in Digits")
            Admin.add_emp(self)

        else:
            mobile_no = int(input("Enter Mobile Number      :    "))
            if len(str(mobile_no)) == 10:
                mail_id = input("Enter employee's mail I'd:    ")
                if "@" and "gmail.com" in mail_id:
                    self.dict1.update({self.emp_id:[self.emp_id,username,password,job_role,salary,mobile_no,mail_id]})
                    self.attendance2.update({self.emp_id:0})
                    print("\nSee Employee Dictionary:\n",self.dict1)
                    print("\n!!_ _ _ _ Employee Added Successfully _ _ _ _!!")
                else:
                    print("\nOops!! Invalid E-mail I'd ....\nE-mail I'd Should Contain '@' and 'gmail.com' \nEnter Again")
                    Admin.add_emp(self)
            else:
                print("\nOops!! Please Enter 10 digit Mobile number\nEnter Again")
                Admin.add_emp(self)
      


    def promote_emp(self):
        print("\n     ------->>    Promote Employee    <<-------         \n")
        try:
            emp_id = int(input("Enter employee I'd       :   "))
            if emp_id in self.dict1:
                job_role = input("Enter employee's job role:   ")
                salary = int(input("Enter employee's salary  :   "))
            else:
                print("\nOops!! ---->> Employee I'd is Not Found ....\nEnter Again\n")
                Admin.promote_emp(self)
        except:
                print("\nOops Invalid Input ....\nEnter Input Only in Digits")
                Admin.promote_emp(self)
        else:
                self.dict1[emp_id][3] = job_role
                self.dict1[emp_id][4] = salary
                print(f"Promoted Details : {self.dict1[emp_id]}")
                print("\n_ _ _ _ Employee Promoted Successfully _ _ _ _")



    """"This Method Display Details Of An Employee"""
    def display_details(self):
        emp_id = int(input("\nEnter Employee's I'd :  "))
        if emp_id in self.dict1:
            print(f"\nI'd        :   {self.dict1[emp_id][0]}\nUsername   :   {self.dict1[emp_id][1]}\nPassword   :   {self.dict1[emp_id][2]}\nJob Role   :   {self.dict1[emp_id][3]}\nsalary     :   {self.dict1[emp_id][4]}\nMobile no  :   {self.dict1[emp_id][5]}\nE-mail I'd :   {self.dict1[emp_id][6]}")
            time.sleep(3)            
        else:
            print("\nOops!! ---->> Employee I'd is Not Found ....\nEnter Again\n")
            Admin.display_details(self)



    """"This Method Remove an Employee"""
    def remove_emp(self):
        print("\n     ------->>    Remove Employee    <<-------         \n")
        emp_id = int(input("Enter Employee's I'd :  "))
        if emp_id in self.dict1:
            self.dict1.pop(emp_id)
            print(self.dict1)     #to check the data
            print("\n_ _ _ _ Employee Removed Successfully _ _ _ _ ")
        else:
            print("\nOops!! ---->> Employee I'd is Not Found\nenter Again\n")
            Admin.remove_emp(self)



    def admin_login(self):
        try:
            while True:
                print("\n- - - - - - - - - - - - - - - ")
                print("\nHello Admin ( *-* )\nChoose the following option:\n\n1.Add Employee\n2.Promote Employee\n3.Display Employee details\n4.Remove Employee\n5.Exit\n")
                choice2 = int(input("Enter Your Choice : "))
                if choice2 == 1:
                    Employee.add_emp(self)
                elif choice2 == 2:
                    Employee.promote_emp(self)
                # elif choice2 == 3:
                #     Employee.update_details(self)
                elif choice2 == 3:
                    Employee.display_details(self)
                elif choice2 == 4:
                    Employee.remove_emp(self)
                elif choice2 == 5:
                    break
                else:
                    print("OOPS!!   Invalid option...")
        except:
            print("\nOops ---->> Error Occurred")


class Employee(Admin):
    def __init__(self):
        super().__init__()
        # self.attendance2 = {101:10}

    def attendance(self):
        print("\n     ------->>    Employee Attendance    <<-------         \n")
        try:
            emp_id = int(input("Enter Employee's I'd :     "))
            if emp_id in self.attendance2:
                attend = input("Enter present/absent :     ")
                if attend == "present" or attend == "p":
                    update = self.attendance2[emp_id] 
                    self.attendance2[emp_id] = update+1
                    print("Total Present days   :    ",self.attendance2[emp_id])
                elif attend == "absent" or attend == "a":
                    pass
                else:
                    print("\nOops!!  Invalid Input ....\n")
                    Employee.attendance(self)
            else:
                print("\nOops!! Employee is Not Found\nEnter Again\n")
                Employee.attendance(self)
        except:
            print("\nOops Error Occurred ....")
            Employee.attendance(self)

    def monthly_salary(self):
        print("\n     ------->>    Employee's Salary    <<-------         \n")
        try:
            emp_id = int(input("Enter Employee's I'd :      "))
            if emp_id in self.dict1 and self.attendance2:
                salary = self.dict1[emp_id][4]
                print(f"\nYour Fixed Salary is {salary} Rupees.")
                per_day = salary/30
                # print("Per Day salary:   ",per_day)
                print(f"\nTotal Working days :    {self.attendance2[emp_id]}")
                total = self.attendance2[emp_id]*per_day
                print(f"\nTotal Current Month's Salary is {total} Rupees.")
                print("\n\t  <<---  Keep Working Champ  --->>")
                print("\n\t<<- - - - - - ( * - * ) - - - - - ->>")
                time.sleep(2)
            else:
                print("Oops!! Employee id Not Found ....")
                Employee.monthly_salary(self)
        except:
            print("\nOops Error Occurred ....")
            Employee.monthly_salary(self)


    """"This Method Updates The Details Of an Employee"""
    def update_details(self):
        print("\n     ------->>    Update Employee Details    <<-------         \n")
        try:
            emp_id = int(input("Enter employee's I'd:   "))
            if emp_id in self.dict1:
                mobile_no = int(input("Enter Mobile Number     :     "))
                if len(str(mobile_no)) == 10:
                    rand = random.randrange(1111,9999)
                    print(f"OTP to verify Your Mobile Number\n\t** {rand} **\n")
                    verify = int(input("Enter the Above OTP:    "))
                    if rand == verify:
                        self.dict1[emp_id][5] = mobile_no
                        print("Mobile Number Updated ....")
                        mail_id = input("\nEnter employee's mail I'd :     ")
                        if "@" and "gmail.com" in mail_id:
                            rand2 = random.randrange(1111,9999)
                            print(f"OTP to Verify Your E-mail I'd\n\t** {rand2} **\n")
                            verify2 = int(input("Enter the Above OTP:    "))
                            if rand2 == verify2:
                                self.dict1[emp_id][6] = mail_id
                                print("E-mail I'd Updated ....")
                                print(f"\nupdated details:\n{self.dict1}")
                                print("\n_ _ _ _ Employee's Detail's Updated Successfully _ _ _ _")
                            else:
                                print("Entered OTP is invalid ....")
                                Admin.update_details(self)
                        else:
                            print("Oops!! ---->> Invalid E-mail I'd ....\nEnter again")
                            Admin.update_details(self)
                    else:
                        print("Entered OTP is Invalid ....")
                        Admin.update_details(self)
                else:
                    print("Oops!! ---->> Enter 10 Digit Number Only ....\nEnter again")
                    Admin.update_details(self)
            else:
                print("Oops Employee I'd is Not Found ....")
                Admin.update_details(self)

        except:
            print("\nOops ---->> Error Occurred")
            Admin.update_details(self)


    def employee_login(self):
        while True:
            try:
                print("\n\nHello Employee ( *-* )\nChoose the following option:\n\n1.Display Details\n2.Update Details\n3.Attendance\n4.Monthly Salary\n5.Exit\n")
                choice = int(input("Enter Your Choice :     "))
                if choice == 1:
                    Admin.display_details(self)
                elif choice == 2:
                    Employee.update_details(self)
                elif choice == 3:
                    Employee.attendance(self)
                elif choice == 4:
                    Employee.monthly_salary(self)
                elif choice == 5:
                    break
                else:
                    print("Invalid Input ....")
            except:
                print("\nOops!!  Enter Valid Input ....")

emp = Employee()

while True:
    print("\n\n \t\t<<------- * # *  Welcome In Employee Management System  * # * ------>>\n")
    print("\nChoose Login Option\n1.Admin \n2.Employee \n3.Exit")
    choice = int(input("\nEnter your choice:  "))
    if choice == 1:
        username = input("\nEnter admin's username:   ")
        if username == "admin":
            password = input("Enter admin's password:   ")
            if password == "admin":
                print("\n---> Admin Login Successfully <---\n")
                emp.admin_login()

            else:
                print("Invalid Password....")
        else:
            print("Invalid username....")
    elif choice == 2:
        try:
            emp_id = int(input("Enter Employee's I'd :     "))
            username2 = input("Enter Your Username  :     ")
            if username2 in emp.dict1[emp_id] :
                    password2 = input("Enter Your Password  :     ")
                    if password2 in emp.dict1[emp_id]:
                        print("\n---> Employee Login Successfully <---\n")
                        emp.employee_login()
                        
        except:
            print("\nOops Invalid Login Input ....")

    elif choice == 3:
        print("\n\t<<------ Thanks For Visit ------>>")
        break
    else:
        print("Invalid choice....")

#   whenever I import new module in command prompt and I import in vs code then i Got "ModuleNotFoundError"

