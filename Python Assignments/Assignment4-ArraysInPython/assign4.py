# 1. Program to Create and Display Array Items
def create_and_display_array():
    array = [2, 7, 14, 5, 9]
    print("1. Array items:", array)

# Test the function
create_and_display_array()

# 2. Program to Reverse the Order of Array Items
def reverse_array():
    array = [2, 7, 14, 5, 9]
    reversed_array = array[::-1]
    print("\n2. Reversed Array:", reversed_array)

# Test the function
reverse_array()

# 3. Program to Find the Largest and Smallest Numbers in Array
def find_largest_and_smallest():
    array = [2, 7, 14, 5, 9]
    largest_number = max(array)
    smallest_number = min(array)
    print("\n3. Largest Number:", largest_number)
    print("   Smallest Number:", smallest_number)

# Test the function
find_largest_and_smallest()

# 4. Program to Display Array Element Addition
def array_element_addition():
    array = [2, 7, 14, 5, 9]
    total_sum = sum(array)
    print("\n4. Array Element Addition:", total_sum)

# Test the function
array_element_addition()

# 5. Program to Find Odd or Even Numbers Using Array
def find_odd_or_even():
    array = [2, 7, 14, 5, 9]
    odd_numbers = [num for num in array if num % 2 != 0]
    even_numbers = [num for num in array if num % 2 == 0]
    print("\n5. Odd Numbers:", odd_numbers)
    print("   Even Numbers:", even_numbers)

# Test the function
find_odd_or_even()

# 6. Program to Calculate the Length of a String
def calculate_string_length():
    input_string = "Python is great!"
    string_length = len(input_string)
    print("\n6. Length of the String:", string_length)

# Test the function
calculate_string_length()

# 7. Program to Count Character Frequency in a String
def count_character_frequency():
    input_string = "programming"
    character_frequency = {}
    for char in input_string:
        character_frequency[char] = character_frequency.get(char, 0) + 1
    print("\n7. Character Frequency:", character_frequency)

# Test the function
count_character_frequency()
