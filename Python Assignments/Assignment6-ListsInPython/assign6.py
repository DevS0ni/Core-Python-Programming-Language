# 1. Program to Display Characters at Even Index
def display_even_index_characters():
    user_input = input("Enter a string: ")
    result = user_input[::2]
    print(f"\n1. Characters at Even Index: {result}")

# Test the function
display_even_index_characters()

# 2. Program to Check if First and Last Numbers in a List are Same
def check_first_last_same(numbers):
    result = numbers[0] == numbers[-1]
    print(f"\n2. First and Last Numbers are Same: {result}")

# Test the function
numbers_2 = [1, 2, 3, 4, 1]
check_first_last_same(numbers_2)

# 3. Program to Print Numbers Divisible by 5
def print_divisible_by_5(numbers):
    divisible_by_5 = [num for num in numbers if num % 5 == 0]
    print("\n3. Numbers Divisible by 5:", divisible_by_5)

# Test the function
numbers_3 = [15, 20, 25, 30, 35]
print_divisible_by_5(numbers_3)

# 4. Program to Create a Third List with Odd from First and Even from Second
def create_third_list(list1, list2):
    third_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]
    print("\n4. Third List with Odd from First and Even from Second:", third_list)

# Test the function
list1_4 = [1, 3, 5, 7, 9]
list2_4 = [2, 4, 6, 8, 10]
create_third_list(list1_4, list2_4)

# 5. Program to Remove and Add Elements in a List
def manipulate_list(input_list):
    element_at_index_4 = input_list.pop(4)
    input_list.insert(2, element_at_index_4)
    input_list.append(element_at_index_4)
    print("\n5. List after Manipulation:", input_list)

# Test the function
list_5 = [1, 2, 3, 4, 5, 6]
manipulate_list(list_5)
