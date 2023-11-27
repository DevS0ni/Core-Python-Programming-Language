# 1. Class Student
class Student:
    def __init__(self, studnumber, studname, marks):
        self.studnumber = studnumber
        self.studname = studname
        self.marks = marks
        self.total_marks = sum(marks)
        self.average_marks = self.total_marks / len(marks)

    def display_info(self):
        print("\nStudent Information:")
        print(f"Student Number: {self.studnumber}")
        print(f"Student Name: {self.studname}")
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {self.total_marks}")
        print(f"Average Marks: {self.average_marks}")


# 2. Class Employee
class Employee:
    def __init__(self, employeeno, employeename, employeeid, employeesalary):
        self.employeeno = employeeno
        self.employeename = employeename
        self.employeeid = employeeid
        self.employeesalary = employeesalary

    def display_info(self):
        print("\nEmployee Information:")
        print(f"Employee Number: {self.employeeno}")
        print(f"Employee Name: {self.employeename}")
        print(f"Employee ID: {self.employeeid}")
        print(f"Employee Salary: {self.employeesalary}")


# 3. Class Library
class Library:
    def __init__(self, bookname, authorname, bookprice):
        self.bookname = bookname
        self.authorname = authorname
        self.bookprice = bookprice

    def display_info(self):
        print("\nLibrary Information:")
        print(f"Book Name: {self.bookname}")
        print(f"Author Name: {self.authorname}")
        print(f"Book Price: {self.bookprice}")


# 4. Class Product
class Product:
    def __init__(self, productnumber, productname, productprice, batchnumber):
        self.productnumber = productnumber
        self.productname = productname
        self.productprice = productprice
        self.batchnumber = batchnumber

    def display_info(self):
        print("\nProduct Information:")
        print(f"Product Number: {self.productnumber}")
        print(f"Product Name: {self.productname}")
        print(f"Product Price: {self.productprice}")
        print(f"Batch Number: {self.batchnumber}")


# 5. Class Bank
class Bank:
    def __init__(self, bankname, branchname, accountnumber, accounttype, holdername, age, city, gender):
        self.bankname = bankname
        self.branchname = branchname
        self.accountnumber = accountnumber
        self.accounttype = accounttype
        self.holdername = holdername
        self.age = age
        self.city = city
        self.gender = gender

    def display_info(self):
        print("\nBank Information:")
        print(f"Bank Name: {self.bankname}")
        print(f"Branch Name: {self.branchname}")
        print(f"Account Number: {self.accountnumber}")
        print(f"Account Type: {self.accounttype}")
        print(f"Holder Name: {self.holdername}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Gender: {self.gender}")


# Test the classes
# 1. Test Student Class
student1 = Student(1, "John Doe", [80, 90, 75])
student1.display_info()

# 2. Test Employee Class
employee1 = Employee(101, "Alice", "E123", 50000)
employee1.display_info()

# 3. Test Library Class
book1 = Library("Python Programming", "Guido van Rossum", 30.50)
book1.display_info()

# 4. Test Product Class
product1 = Product(1001, "Laptop", 1200, "B123")
product1.display_info()

# 5. Test Bank Class
account1 = Bank("ABC Bank", "Main Branch", "A12345", "Savings", "John Doe", 30, "New York", "Male")
account1.display_info()
