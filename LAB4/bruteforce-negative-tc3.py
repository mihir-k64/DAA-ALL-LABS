def brute_force_multiplication(x, y):
    if isinstance(x, bool) or isinstance(y, bool):
        raise TypeError("Invalid input: One of the inputs is a boolean. Multiplication requires integers.")
    
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both inputs must be integers for multiplication.")
    
    return x * y

try:
    result = brute_force_multiplication(True, 5678) 
    print(f"Multiplication result: {result}")
except TypeError as e:
    print(f"Error: {e}")
