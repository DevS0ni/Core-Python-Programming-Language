# 1. Program to Create a Tuple
def create_tuple():
    my_tuple = ()
    print("1. Created Tuple:", my_tuple)

# Test the function
create_tuple()

# 2. Program to Create a Tuple with Different Data Types
def create_mixed_type_tuple():
    mixed_tuple = (1, "hello", 3.14, True)
    print("\n2. Mixed Type Tuple:", mixed_tuple)

# Test the function
create_mixed_type_tuple()

# 3. Program to Unpack a Tuple in Several Variables
def unpack_tuple():
    my_tuple = (10, 20, 30)
    var1, var2, var3 = my_tuple
    print("\n3. Unpacked Variables:", var1, var2, var3)

# Test the function
unpack_tuple()

# 4. Program to Add an Item in a Tuple
def add_item_to_tuple():
    original_tuple = (1, 2, 3)
    added_tuple = original_tuple + (4,)
    print("\n4. Tuple After Adding Item:", added_tuple)

# Test the function
add_item_to_tuple()

# 5. Program to Convert a Tuple to a String
def convert_tuple_to_string():
    my_tuple = ('P', 'y', 't', 'h', 'o', 'n')
    string_result = ''.join(my_tuple)
    print("\n5. Tuple Converted to String:", string_result)

# Test the function
convert_tuple_to_string()

# 6. Program to Get the 4th and 4th Element from Last of a Tuple
def get_elements_from_tuple():
    my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
    fourth_element = my_tuple[3]
    fourth_from_last = my_tuple[-4]
    print("\n6. 4th Element and 4th Element from Last:", fourth_element, fourth_from_last)

# Test the function
get_elements_from_tuple()

# 7. Program to Check Whether an Element Exists Within a Tuple
def check_element_existence():
    my_tuple = (1, 2, 3, 4, 5)
    element_to_check = 3
    exists = element_to_check in my_tuple
    print("\n7. Element Existence Check:", exists)

# Test the function
check_element_existence()

# 8. Program to Find the Index of an Item in a Tuple
def find_index_of_item():
    my_tuple = ('a', 'b', 'c', 'd', 'e')
    item_to_find = 'c'
    index = my_tuple.index(item_to_find)
    print("\n8. Index of Item in Tuple:", index)

# Test the function
find_index_of_item()

# 9. Program to Print a Tuple with String Formatting
def print_tuple_with_formatting():
    sample_tuple = (100, 200, 300)
    formatted_output = "This is a tuple {}".format(sample_tuple)
    print("\n9. Tuple with String Formatting:", formatted_output)

# Test the function
print_tuple_with_formatting()
