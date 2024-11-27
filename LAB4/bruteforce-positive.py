import random

def generate_random_number(digit_length):
    return random.randint(10**(digit_length-1), (10**digit_length) - 1)

def brute_force_multiplication(x, y):
    return x * y

digit_lengths = [10, 50, 100, 500, 1000]

for digits in digit_lengths:
    num1 = generate_random_number(digits)
    num2 = generate_random_number(digits)
    
    result = brute_force_multiplication(num1, num2)
    
    print(f"Multiplication of two {digits}-digit numbers:")
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Product: {result}\n")
