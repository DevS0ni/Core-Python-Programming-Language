import math

# 1. Celsius to Fahrenheit and Fahrenheit to Celsius conversion
def celsius_to_fahrenheit(celsius):
    return (9 * celsius / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (5 * (fahrenheit - 32)) / 9

# Test the conversions
celsius_value = 25
fahrenheit_value = 77

print(f"{celsius_value} Celsius is {celsius_to_fahrenheit(celsius_value)} Fahrenheit")
print(f"{fahrenheit_value} Fahrenheit is {fahrenheit_to_celsius(fahrenheit_value)} Celsius")

# 2. Print Student Information
def print_student_info(student_number, student_name, marks):
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)

    print(f"\nStudent Number: {student_number}")
    print(f"Student Name: {student_name}")
    print(f"Marks: {marks}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks}")

# Test the function
student_number = 101
student_name = "John Doe"
subject_marks = [85, 90, 78, 92]

print_student_info(student_number, student_name, subject_marks)

# 3. Calculate Cube of a Number
def calculate_cube(number):
    return number ** 3

# Test the function
input_number = 2
result = calculate_cube(input_number)
print(f"\nThe cube of {input_number} is {result}")

# 4. Calculate Area of Trapezoid
def calculate_trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h

# Test the function
parallel_side_a = 5
parallel_side_b = 8
height = 4

area_result = calculate_trapezoid_area(parallel_side_a, parallel_side_b, height)
print(f"\nThe area of the trapezoid is {area_result}")

# 5. Calculate Volume of Spherical Cap
def calculate_spherical_cap_volume(radius, height):
    return (math.pi / 6) * (3 * radius ** 2 + height ** 2) * height

# Test the function
sphere_radius = 5
cap_height = 2

volume_result = calculate_spherical_cap_volume(sphere_radius, cap_height)
print(f"\nThe volume of the spherical cap is {volume_result}")

# 6. Calculate Total Surface Area of Rectangular Parallelepiped
def calculate_rectangular_parallelepiped_area(a, b, c):
    return 2 * (a * b + a * c + b * c)

# Test the function
side_a = 4
side_b = 6
side_c = 8

area_result = calculate_rectangular_parallelepiped_area(side_a, side_b, side_c)
print(f"\nThe total surface area of the rectangular parallelepiped is {area_result}")
