# 1. Program to Determine Positive, Negative, or Zero
def check_number_type(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Test the function
entered_number_1 = 7
print(f"1. The number {entered_number_1} is {check_number_type(entered_number_1)}")

# 2. Program to Determine Odd, Even, or Zero
def check_odd_even(number):
    if number % 2 == 0 and number != 0:
        return "Even"
    elif number % 2 != 0:
        return "Odd"
    else:
        return "Zero"

# Test the function
entered_number_2 = -3
print(f"2. The number {entered_number_2} is {check_odd_even(entered_number_2)}")

# 3. Program to Find the Greater Number
def find_greater_number(a, b, c):
    return max(a, b, c)

# Test the function
num_1 = 14
num_2 = 27
num_3 = 19
print(f"3. The greater number among {num_1}, {num_2}, and {num_3} is {find_greater_number(num_1, num_2, num_3)}")

# 4. Program to Compute Rebate
def compute_rebate(customer_id, purchase_amount):
    if purchase_amount <= 5000:
        rebate_percentage = 0.03
    elif 5000 < purchase_amount <= 10000:
        rebate_percentage = 0.09
    else:
        rebate_percentage = 0.12

    rebate = rebate_percentage * purchase_amount
    return customer_id, purchase_amount, rebate

# Test the function
customer_id_4 = 101
purchase_amount_4 = 8000
print(f"4. Customer ID: {customer_id_4}, Purchase Amount: {purchase_amount_4}, Rebate: {compute_rebate(customer_id_4, purchase_amount_4)[2]}")

# 5. Program to Calculate Bill Amount for a Bookshop
def calculate_bookshop_bill(science_subjects, commerce_subjects, arts_subjects):
    discount_science = 0.02
    discount_commerce = 0.03
    discount_arts = 0.04
    discount_gross_amount = 0.025
    threshold_gross_amount = 200

    gross_amount = science_subjects + commerce_subjects + arts_subjects
    total_discount = discount_gross_amount * gross_amount if gross_amount > threshold_gross_amount else 0

    bill_amount = (science_subjects * (1 - discount_science) +
                   commerce_subjects * (1 - discount_commerce) +
                   arts_subjects * (1 - discount_arts)) * (1 - discount_gross_amount)

    return bill_amount

# Test the function
bill_amount_5 = calculate_bookshop_bill(300, 400, 500)
print(f"5. The bill amount for the bookshop is {bill_amount_5}")

# 6. Program to Calculate Net Salary in a Payroll System
def calculate_net_salary(basic_pay, city_type):
    da_percentage = 0.6 if basic_pay <= 8000 else 0.5
    hra_percentage_metro = 0.3
    hra_percentage_non_metro = 0.15
    cca = 300
    pf_percentage = 0.06

    da = da_percentage * basic_pay
    hra = hra_percentage_metro * basic_pay if city_type == "Metro" else hra_percentage_non_metro * basic_pay
    pf = pf_percentage * basic_pay

    total_income = basic_pay + da + hra + cca
    net_salary = total_income - pf

    return total_income, net_salary

# Test the function
basic_pay_6 = 9000
city_type_6 = "Metro"
total_income_6, net_salary_6 = calculate_net_salary(basic_pay_6, city_type_6)
print(f"6. Total Income: {total_income_6}, Net Salary: {net_salary_6}")

# 7. Program to Find Numbers Divisible by 7 and Multiple of 5
divisible_by_7_and_multiple_of_5 = [num for num in range(1500, 2701) if num % 7 == 0 and num % 5 == 0]
print(f"\n7. Numbers divisible by 7 and multiple of 5 between 1500 and 2700: {divisible_by_7_and_multiple_of_5}")
