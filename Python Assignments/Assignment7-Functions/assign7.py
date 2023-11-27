# 1. Function to Find the Max of Three Numbers
def find_max_of_three(num1, num2, num3):
    max_number = max(num1, num2, num3)
    return max_number

# Test the function
result_1 = find_max_of_three(5, 10, 3)
print(f"1. Max of Three Numbers: {result_1}")

# 2. Function to Sum All Numbers in a List
def sum_all_numbers(numbers):
    total_sum = sum(numbers)
    return total_sum

# Test the function
numbers_2 = [8, 2, 3, 0, 7]
result_2 = sum_all_numbers(numbers_2)
print(f"\n2. Sum of Numbers in List: {result_2}")

# 3. Function to Multiply All Numbers in a List
def multiply_all_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Test the function
numbers_3 = [8, 2, 3, -1, 7]
result_3 = multiply_all_numbers(numbers_3)
print(f"\n3. Product of Numbers in List: {result_3}")

# 4. Program to Reverse a String
def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

# Test the function
string_4 = "1234abcd"
result_4 = reverse_string(string_4)
print(f"\n4. Reversed String: {result_4}")

# 5. Program to Print Even Numbers from a List
def print_even_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers

# Test the function
list_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result_5 = print_even_numbers(list_5)
print(f"\n5. Even Numbers in List: {result_5}")
