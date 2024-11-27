def brute_force_multiplication(x, y):
    if isinstance(x, complex) or isinstance(y, complex):
        raise TypeError("Invalid input: One of the inputs is a complex number. Multiplication requires integers.")
    
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both inputs must be integers for multiplication.")
    
    return x * y

try:
    result = brute_force_multiplication(3 + 4j, 5678)  
    print(f"Multiplication result: {result}")
except TypeError as e:
    print(f"Error: {e}")

