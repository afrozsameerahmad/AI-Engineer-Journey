# we write class name in pascal case

# rules for creating class
# 1. class name should be in pascal case
# 2. class should have a constructor
# 3. constructor should have self as first parameter
# 4. without creating object we cannot access the class variables and methods
class Atm:
    # constructor is special function it have super power to create object and initialize the object 
    # we cant call constructor directly but we can call it indirectly by creating object
    #in simple we dont need to call constructor it will be called automatically when we create object
    #jitni baar hum object banayenge utni baar constructor call hoga
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
        
    def menu(self):
        while True:
            user_input = input("""
            Hi How i can help you?
            1.Press 1 to create pin
            2.Press 2 to change pin
            3.Press 3 to check balance
            4.Press 4 to withdraw money
            5.Press 5 to deposit money
            6.Press 6 to exit
            """)

            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.change_pin()
            elif user_input == '3':
                self.check_balance()
            elif user_input == '4':
                self.withdraw_money()
            elif user_input == '5':
                self.deposit_money()
            elif user_input == '6':
                print("Thank you for using ATM")
                break
            else:
                print("Invalid input")
       
             
             
            
            
    def create_pin(self):
        user_pin=input("Enter your new pin: ")
        self.pin = user_pin
        
        
        user_balance=int(input("Enter your initial balance: "))
        self.balance = user_balance
        print("Pin created successfully")
    
    def change_pin(self):
        old_pin=input("enter old pin")
        if old_pin == self.pin:
            new_pin=input("enter new pin")
            self.pin = new_pin
            print("Pin changed successfully")
        else:
            print("Nhi krne de skte bhai")

    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print("Your current balance is:", self.balance)
        else:
            print("Chal nikal yha se ")

    def withdraw_money(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Withdrawal successful")
                print("Remaining balance:", self.balance)
            else:
                print("Gareeb aadmi ho kya? itna paisa kaha se aaya")
        else:
            print("bhai pin yaad krke rkh")

    def deposit_money(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            amount = int(input("Enter amount to deposit: "))
            self.balance = self.balance + amount
            print("Deposit successful")
            print("Updated balance:", self.balance)
        else:
            print("bhai pin yaad krke rkh")
             
            
obj=Atm()

