def matrix_chain_multiplication(dimensions):
    if len(dimensions) < 2:
        return -1, "Matrix dimension array length should be N-1"
    
    if any(k <= 0 for k in dimensions):
        return -1, "Matrix dimensions must be positive"
    
    for i in range(len(dimensions) - 2):
        if dimensions[i + 1] != dimensions[i + 2]:
            return -1, "Incompatible matrix dimensions for multiplication"
    
    n = len(dimensions) - 1
    
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if q < dp[i][j]:
                    dp[i][j] = q
                    split[i][j] = k
    
    def get_optimal_order(i, j):
        if i == j:
            return f"A{i + 1}"
        k = split[i][j]
        left_order = get_optimal_order(i, k)
        right_order = get_optimal_order(k + 1, j)
        return f"({left_order} x {right_order})"
    
    optimal_order = get_optimal_order(0, n - 1)
    return dp[0][n - 1], optimal_order

def test_empty_list():
    matrices = []
    cost, order = matrix_chain_multiplication(matrices)
    print(f"Test Case 1: Empty List")
    print(f"Cost: {cost}, Order: {order}\n")

def test_single_matrix():
    matrices = [5, 7]
    cost, order = matrix_chain_multiplication(matrices)
    print(f"Test Case 2: Single Matrix")
    print(f"Cost: {cost}, Order: {order}\n")

def test_incompatible_dimensions():
    matrices = [5, 7, 6, 8, 7, 9]
    cost, order = matrix_chain_multiplication(matrices)
    print(f"Test Case 3: Incompatible Matrix Dimensions")
    print(f"Cost: {cost}, Order: {order}\n")

def test_invalid_dimensions():
    matrices = [5, 7, -6, 8, 7, 9]
    cost, order = matrix_chain_multiplication(matrices)
    print(f"Test Case 4: Invalid Matrix Dimensions")
    print(f"Cost: {cost}, Order: {order}\n")

def test_non_square_matrices():
    matrices = [5, 7, 7, 5, 5, 7]
    cost, order = matrix_chain_multiplication(matrices)
    print(f"Test Case 5: Non-square Matrices")
    print(f"Cost: {cost}, Order: {order}\n")

test_empty_list()
test_single_matrix()
test_incompatible_dimensions()
test_invalid_dimensions()
test_non_square_matrices()
