def brute_force_multiplication(x, y):
    if isinstance(x, str) or isinstance(y, str):
        raise TypeError("Invalid input: One of the inputs is text. Multiplication requires numbers.")
    
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both inputs must be integers for multiplication.")
    
    return x * y

try:
    result = brute_force_multiplication("mihir", 5678)  
    print(f"Multiplication result: {result}")
except TypeError as e:
    print(f"Error: {e}")
