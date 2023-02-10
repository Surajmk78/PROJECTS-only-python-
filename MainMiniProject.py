import random
import maskpass
class ATM():
    def __init__(self):
        self.customer={1234567890:["madan",1231,1000],1234567891:["sai",123,4000],1234567892:["rahul",1234,10000]}
        self.balance=100000
        
    def Login(self):
        print("\n\n*********************WELCOME TO ATM MACHINE*******************************\n")
        name=int(input("enter your account number:"))
        if name in self.customer:
            User_Account=input("Enter Your name:")
            for i in self.customer.values():
                if User_Account in i:
                    print("\n\n********valid account*********\n")
                    user_try_pin=3
                    while (user_try_pin !=0):
                        User_pin=maskpass.askpass("Enter your 4 digitpin:")
                        for i in self.customer.values():
                            if User_pin in i:
                                print("\n**********************WELCOME TO YOUR BANK ACCOUNT************************\n")
                                print("_____MADAN C CHOUDHARY______\n")
                                self.HomePage()
                            else:
                                user_try_pin-=1 
                                print(f"PIN incorrect! Number of tries left -{user_try_pin}")   
                    else:
                        print("\n*******You have been logged out. Thank you!**************")
                else:
                    print("\n*****************invalid account number*********************\n\n")
        else:
            print("plz enter correct name")
    def Admin(self):
        print("\n\n*********************WELCOME TO ATM MACHINE MANAGER*******************************\n\n")
        while True:
            name=input("enter your name:")
            if name=="manager":
                Account=int(input("\nEnter Your Account Number:"))
                if Account==123456:
                    print("\n\n********valid account*********\n")
                    try_pin=3
                    while (try_pin !=0):
                        pin=maskpass.askpass("Enter your 4 digitpin:",mask="*")
                        if pin==0000:
                            print("\n**********************WELCOME TO YOUR BANK************************\n")
                            print("\n_____MANAGER______\n")
                            self.adminop()
                        else:
                            try_pin-=1 
                            print(f"PIN incorrect! Number of tries left -{try_pin}")   
                    else:
                        print("\n*******You have been logged out. Thank you!**************")
                else:
                    print("\n*****************invalid account number*********************\n\n")
            else:        
                print("\n**************plz enter correct name*************\n\n")
                break
        else:
            print()
            

    def adminop(self):    
        while True:
            print("*"*50)
            print("1:DEPOSIT \n\n2:EXIT")
            print("*"*50)
            choice=input("enter your choice:")
            if choice=="1":
                self.DEPOSIT()
            elif choice=="2":
                self.EXIT()
            else:
                print("******************invlaid choice*****************")
                self.adminop()    


    def DEPOSIT(self):
        var= int(input("\nEnter amount deposit : "))
        print(f"*************\nDepositing Rs.{var}***********")
        confirm = input("\nConfirm? Y/N > ")
        if confirm in ('Y', 'y'): 
            self.balance+=var
            print(f"\nAmount deposited - Rs.{var}\n")
            print(f"\nUpdated balance - Rs.{self.balance}\n")
            self.adminop()
        else:
            print("\n****************Cancelling transaction...")
            print("\n****************Transaction Cancelled!\n\n")
            self.HomePage()

    def EXIT(self):
        print("\nExiting...")
        print("\nYou have been logged out. Thank you!\n\n")
        exit()

    def HomePage(self):
        while(True):
            print("....................")
            print("\n1:Admin_page \n\n2:Withdraw_Amount \n\n3:Deposit_Amount \n\n4:Check_Balance  \n\n5.Logout")
            print("....................")
            choice=(input("\nEnter your choice :"))
            if choice=="1":
                self.Admin()
            elif choice=="2":
                self.Withdraw_Amount()    
            elif choice=="3":
                self.Deposit_Amount()
            elif choice=="4":
                self.Check_Balance()
            elif choice=="5":
                self.Logout()
            else:
                print(" \n x-x-x-x  Enter valid choice  x-x-x-x  \n ") 
            break

    def Withdraw_Amount(self):
            withdraw_amt = int(input("\nEnter the amount you wish to withdraw : "))
            for i in self.customer.values():
                if withdraw_amt> i:
                    print(f"\nCan't withdraw Rs.{ withdraw_amt}\n")
                    print("\n**************Please check your bank balance*********** \nTransaction declined. Insufficient funds. Deposit some money first.\n")
                else:
                    print(f"\nWithdrawing Rs.{withdraw_amt}\n")
                    confirm = input("\nConfirm? Y/N : ")
                
                    if confirm in ("Y","y"):
                        self.customer-=withdraw_amt
                        print(f"\nAmount withdrawn - Rs.{ withdraw_amt}")
                        print(f"\nRemaining balance - Rs.{self.customer}\n")
                    else:
                        print("\n******************Cancelling transaction...\n")
                        print("\n*****************Transaction Cancelled!\n\n") 
                     

    def Deposit_Amount(self):
            deposit_amt = int(input("\nEnter the amount you wish to deposit : "))
            print(f"\nDepositing Rs.{deposit_amt}")
            confirm = input("\nConfirm? Y/N > ")
            if confirm in ('Y', 'y'): 
                self.customer+=deposit_amt
                print(f"\nAmount deposited - Rs.{deposit_amt}\n")
                print(f"\nUpdated balance - Rs.{self.customer}\n")
            else:
                print("\n****************Cancelling transaction...")
                print("\n****************Transaction Cancelled!\n\n")
                 
    def Check_Balance(self):
            print("\nLoading Account Balance...\n")
            print(f"\nYour current balance is Rs.{self.customer.values(3)}\n")     
    


    def Logout(self):
        print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)}
              Account Withdraw_Amount:{self.Withdraw_Amount}
              Account Deposit_Amount:{self.Deposit_Amount}                           
              Thanks for choosing us as your bank                  
          ******************************************
          """)
        print("\nExiting...")
        print("\nYou have been logged out. Thank you!\n\n")
        exit()



obj1=ATM()
obj1.HomePage()        