def brute_force_multiplication(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both inputs must be integers for multiplication, here one number is string which is not allowed.")
    
    return x * y

try:
    result = brute_force_multiplication("1234", 5678)
    print(f"Multiplication result: {result}")
except TypeError as e:
    print(f"Error: {e}")
