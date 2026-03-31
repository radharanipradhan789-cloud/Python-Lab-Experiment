1# This program defines an Employee class with a parameterized constructor to initialize employee details, a method to calculate travel allowance (TA), dearness allowance (DA), and gross pay (GP) based on the basic pay (BP), and a method to display the employee's details. An example usage of the Employee class is provided at the end of the code.
class Employee:
    # Parameterized constructor
    def __init__(self, empid, ename, bp):
        self.empid = empid
        self.ename = ename
        self.bp = bp  # Basic pay
        self.ta = 0   # Travel allowance
        self.da = 0   # Dearness allowance
        self.gp = 0   # Gross pay

    # Method to calculate TA, DA, and Gross Pay
    def calc(self):
        self.ta = self.bp * 10 / 100   # 10% of basic pay
        self.da = self.bp * 40 / 100   # 40% of basic pay
        self.gp = self.bp + self.ta + self.da

    # Method to display employee details
    def disp(self):
        print(f"ID: {self.empid}, Name: {self.ename}, Basic Pay: {self.bp}, TA: {self.ta}, DA: {self.da}, Gross Pay: {self.gp}")


# Example usage
if __name__ == "__main__":
    # Create an employee object
    emp = Employee(1, "Radharani Pradhan", 20000)
    emp.calc()       # Calculate allowances and gross pay
    emp.disp()       # Display employee details

2# This program defines a Clan class that performs basic arithmetic operations (addition, subtraction, multiplication, and division) on two data attributes. The class includes methods for each operation, and an example usage is provided to demonstrate how to create an instance of the Clan class and call the methods to perform the operations.
class Clan:
    # Constructor
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    # Addition
    def addition(self):
        print("Addition:", self.data1 + self.data2)

    # Subtraction
    def subtraction(self):
        print("Subtraction:", self.data1 - self.data2)

    # Multiplication
    def multiplication(self):
        print("Multiplication:", self.data1 * self.data2)

    # Division
    def division(self):
        if self.data2 != 0:
            print("Division:", self.data1 / self.data2)
        else:
            print("Cannot perform division by zero")


# Example usage
if __name__ == "__main__":
    obj = Clan(10, 12)
    obj.addition()        # 10 + 12 = 22
    obj.subtraction()     # 10 - 12 = -2
    obj.multiplication()  # 10 * 12 = 120
    obj.division()        # 10 / 12 = 0.8333...

3# This program defines a Product class with a constructor to initialize product details, a method to calculate the total amount based on quantity and price, and a method to display the product's details. An example usage of the Product class is provided at the end of the code.
class Product:
    # Constructor
    def __init__(self, pid, pname, quantity, price):
        self.pid = pid         # Product ID
        self.pname = pname     # Product Name
        self.quantity = quantity
        self.price = price
        self.total_amount = 0  # Total amount (quantity * price)

    # Calculate total
    def total(self):
        self.total_amount = self.quantity * self.price

    # Display product details
    def display(self):
        print(f"ID: {self.pid}, Name: {self.pname}, Quantity: {self.quantity}, Price: {self.price}, Total: {self.total_amount}")


# Example usage
if __name__ == "__main__":
    obj = Product(100, "Books", 12, 320)
    obj.total()     # Calculate total amount
    obj.display()   # Display product details

4# This program defines a Bank class that simulates basic banking operations such as depositing money, withdrawing money, and displaying account details. The class has a constructor to initialize the account number, holder's name, and balance. The deposit and withdraw methods update the balance accordingly, while the display method shows the current state of the account. An example usage of the Bank class is provided at the end of the code.
class Bank:
    # Constructor
    def __init__(self, ano, holder):
        self.ano = ano             # Account Number
        self.holder = holder       # Account Holder Name
        self.balance = 0           # Initial balance

    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current Balance: {self.balance}")

    # Withdraw method
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Current Balance: {self.balance}")

    # Display account details
    def display(self):
        print(f"Account No: {self.ano}, Holder: {self.holder}, Balance: {self.balance}")


# Example usage
if __name__ == "__main__":
    obj = Bank(10, "Ravi")
    obj.deposit(100)      # Deposit 100
    obj.withdraw(50)      # Withdraw 50
    obj.display()         # Show account details