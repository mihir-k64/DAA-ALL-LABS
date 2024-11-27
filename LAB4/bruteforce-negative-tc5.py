def brute_force_multiplication(x, y):
    if isinstance(x, float) or isinstance(y, float):
        raise TypeError("Invalid input: One of the inputs is a floating-point number. Multiplication requires integers.")
    
    return x * y

try:
    result = brute_force_multiplication(1234.56, 5678)  
    print(f"Multiplication result: {result}")
except TypeError as e:
    print(f"Error: {e}")
