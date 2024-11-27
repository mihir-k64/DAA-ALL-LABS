def karatsuba(x, y):
    if isinstance(x, bool) or isinstance(y, bool):
        print("Invalid input: multiplication of a boolean with a number is not allowed.")
        raise TypeError("Cannot multiply a boolean with a number.")
    
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

try:
    result = karatsuba(True, 5678)
    print(f"Test result: {result}")
    
except TypeError as e:
    print(e)

