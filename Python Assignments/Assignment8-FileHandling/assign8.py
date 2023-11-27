# 1. Program to Write Numbers 1 to 100 to a Data File NOTES.TXT
with open("NOTES.TXT", "w") as file_1:
    for num in range(1, 101):
        file_1.write(str(num) + "\n")

# 2. Program to Initialize a String and Write it to OUT.TXT
initial_string = "Time is a great teacher but unfortunately it kills all its pupils. Berlioz"
with open("OUT.TXT", "w") as file_2:
    file_2.write(initial_string)

# 3. User-defined Function to Count Alphabets in OUT.TXT
def count_alphabets(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        alphabet_count = sum(char.isalpha() for char in content)
    return alphabet_count

# Test the function for OUT.TXT
result_3 = count_alphabets("OUT.TXT")
print(f"\n3. Number of Alphabets in OUT.TXT: {result_3}")

# 4. Function to Count Blanks in a Text File
def count_blanks(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        blank_count = content.count(" ")
    return blank_count

# Test the function for OUT.TXT
result_4 = count_blanks("OUT.TXT")
print(f"\n4. Number of Blanks in OUT.TXT: {result_4}")

# 5. Function to Count Number of Words in a Text File
def count_words(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        word_count = len(content.split())
    return word_count

# Test the function for OUT.TXT
result_5 = count_words("OUT.TXT")
print(f"\n5. Number of Words in OUT.TXT: {result_5}")
