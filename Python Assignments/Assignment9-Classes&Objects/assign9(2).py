class Student:
    def __init__(self):
        self.admno = 0
        self.sname = ""
        self.eng = 0
        self.math = 0
        self.science = 0
        self.total = 0

    def Takedata(self):
        self.admno = int(input("Enter Admission Number: "))
        self.sname = input("Enter Student Name: ")
        self.eng = int(input("Enter Marks in English: "))
        self.math = int(input("Enter Marks in Math: "))
        self.science = int(input("Enter Marks in Science: "))

    def ctotal(self):
        self.total = self.eng + self.math + self.science

    def Showdata(self):
        print("\nStudent Information:")
        print(f"Admission Number: {self.admno}")
        print(f"Student Name: {self.sname}")
        print(f"Marks in English: {self.eng}")
        print(f"Marks in Math: {self.math}")
        print(f"Marks in Science: {self.science}")
        print(f"Total Marks: {self.total}")


class Batsman:
    def __init__(self):
        self.bcode = 0
        self.bname = ""
        self.innings = 0
        self.notout = 0
        self.runs = 0
        self.batavg = 0

    def readdata(self):
        self.bcode = int(input("Enter Batsman Code: "))
        self.bname = input("Enter Batsman Name: ")
        self.innings = int(input("Enter Innings Played: "))
        self.notout = int(input("Enter Not Out Innings: "))
        self.runs = int(input("Enter Runs Scored: "))

    def calcavg(self):
        self.batavg = self.runs / (self.innings - self.notout)

    def displaydata(self):
        print("\nBatsman Information:")
        print(f"Batsman Code: {self.bcode}")
        print(f"Batsman Name: {self.bname}")
        print(f"Innings Played: {self.innings}")
        print(f"Not Out Innings: {self.notout}")
        print(f"Runs Scored: {self.runs}")
        print(f"Batting Average: {self.batavg:.2f}")


class Book:
    def __init__(self):
        self.book_no = 0
        self.book_title = ""
        self.price = 0.0

    def INPUT(self):
        self.book_no = int(input("Enter Book Number: "))
        self.book_title = input("Enter Book Title: ")
        self.price = float(input("Enter Price per Copy: "))

    def TOTAL_COST(self, copies):
        return copies * self.price

    def PURCHASE(self):
        copies = int(input("Enter the number of copies to be purchased: "))
        total_cost = self.TOTAL_COST(copies)
        print(f"Total Cost to be paid: {total_cost:.2f}")


# Test the classes
# 1. Test Student Class
student = Student()
student.Takedata()
student.ctotal()
student.Showdata()

# 2. Test Batsman Class
batsman = Batsman()
batsman.readdata()
batsman.calcavg()
batsman.displaydata()

# 3. Test Book Class
book = Book()
book.INPUT()
book.PURCHASE()
