import math

# Function to Calculate Area of a Rectangle
def calculate_rectangle_area(base, height):
    return base * height

# Function to Calculate Area of a Square
def calculate_square_area(side):
    return side ** 2

# Function to Calculate Area of a Circle
def calculate_circle_area(radius):
    return math.pi * radius ** 2

# Function to Calculate Surface Area of a Cube
def calculate_cube_area(side):
    return 6 * side ** 2

# Function to Display Menu and Perform Operations
def menu():
    print("Menu:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Cube")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        base = float(input("Enter the base of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        result = calculate_rectangle_area(base, height)
        print(f"Area of Rectangle: {result}")

    elif choice == 2:
        side = float(input("Enter the side of the square: "))
        result = calculate_square_area(side)
        print(f"Area of Square: {result}")

    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        result = calculate_circle_area(radius)
        print(f"Area of Circle: {result}")

    elif choice == 4:
        side_cube = float(input("Enter the side of the cube: "))
        result = calculate_cube_area(side_cube)
        print(f"Surface Area of Cube: {result}")

    else:
        print("Invalid choice. Please choose a number from 1 to 4.")

# Test the menu function
menu()

# Function to Calculate Factorial
def calculate_factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * calculate_factorial(num - 1)

# Test the factorial function
num_factorial = int(input("\nEnter a number for factorial calculation: "))
result_factorial = calculate_factorial(num_factorial)
print(f"Factorial of {num_factorial}: {result_factorial}")

# Function to Check if a Number is Prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Test the prime function
num_prime = int(input("\nEnter a number to check if it's prime: "))
result_prime = is_prime(num_prime)
print(f"{num_prime} is Prime: {result_prime}")
