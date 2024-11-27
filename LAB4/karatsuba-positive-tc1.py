def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    max_len = max(len(str(x)), len(str(y)))
    half_len = max_len // 2
    
    x_high = x // (10 ** half_len)
    x_low = x % (10 ** half_len)
    y_high = y // (10 ** half_len)
    y_low = y % (10 ** half_len)
    
    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba((x_low + x_high), (y_low + y_high))
    z2 = karatsuba(x_high, y_high)
    
    return (z2 * (10 ** (2 * half_len))) + ((z1 - z2 - z0) * (10 ** half_len)) + z0

def get_input_number(digit_length):
    while True:
        try:
            num = input(f"Enter a {digit_length}-digit number: ")
            if len(num) == digit_length and num.isdigit():
                return int(num)
            else:
                print(f"Please enter a valid {digit_length}-digit number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

digit_lengths = [10, 50, 100, 500, 1000]

num1 = get_input_number(digit_lengths[0])  
num2 = get_input_number(digit_lengths[0])  

result = karatsuba(num1, num2)
print(f"The product of the 2 numbers is: {result}")
