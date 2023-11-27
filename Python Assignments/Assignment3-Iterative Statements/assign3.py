# 1. Program to Construct a Pattern
def construct_pattern(rows):
    num = 1
    for i in range(rows):
        for j in range(i + 1):
            print(num, end=" ")
            num += 1
        print()

# Test the function
print("1. Constructing the Pattern:")
construct_pattern(4)
print()

# 2. Program to Count Even and Odd Numbers
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

# Test the function
numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count_2, odd_count_2 = count_even_odd(numbers_2)
print(f"2. Even numbers: {even_count_2}, Odd numbers: {odd_count_2}")

# 3. Program to Generate Fibonacci Series
def fibonacci_series(limit):
    fib_series = [0, 1]
    while fib_series[-1] + fib_series[-2] <= limit:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Test the function
limit_3 = 50
fibonacci_result_3 = fibonacci_series(limit_3)
print(f"3. Fibonacci Series up to {limit_3}: {fibonacci_result_3}")

# 4. Program to Calculate Factorial
def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

# Test the function
num_4 = 5
factorial_result_4 = calculate_factorial(num_4)
print(f"4. {num_4}! = {' * '.join(map(str, range(1, num_4 + 1)))} = {factorial_result_4}")

# 5. Program to Calculate Series
def calculate_series(num):
    result = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            result -= i
        else:
            result += i
    return result

# Test the function
num_5 = 5
series_result_5 = calculate_series(num_5)
print(f"5. {'+'.join([str(i) if i % 2 != 0 else '-' + str(i) for i in range(1, num_5 + 1)])} = {series_result_5}")
