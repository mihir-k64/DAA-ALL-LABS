def matrix_chain_multiplication(dimensions):
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

def test_meteorological_data():
    matrices_1 = [4, 7, 4, 7, 4, 7]
    cost_1, order_1 = matrix_chain_multiplication(matrices_1)
    print(f"Test Case 1:\nMinimum number of scalar multiplications: {cost_1}")
    print(f"Optimal multiplication order: {order_1}\n")

    matrices_2 = [3, 7, 3, 7, 3, 7, 3, 7]
    cost_2, order_2 = matrix_chain_multiplication(matrices_2)
    print(f"Test Case 2:\nMinimum number of scalar multiplications: {cost_2}")
    print(f"Optimal multiplication order: {order_2}\n")

    matrices_3 = [5, 7, 5, 7, 5, 7, 5, 7, 5, 7]
    cost_3, order_3 = matrix_chain_multiplication(matrices_3)
    print(f"Test Case 3:\nMinimum number of scalar multiplications: {cost_3}")
    print(f"Optimal multiplication order: {order_3}\n")

    matrices_4 = [6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7]
    cost_4, order_4 = matrix_chain_multiplication(matrices_4)
    print(f"Test Case 4:\nMinimum number of scalar multiplications: {cost_4}")
    print(f"Optimal multiplication order: {order_4}\n")

    matrices_5 = [3, 7, 3, 7]
    cost_5, order_5 = matrix_chain_multiplication(matrices_5)
    print(f"Test Case 5:\nMinimum number of scalar multiplications: {cost_5}")
    print(f"Optimal multiplication order: {order_5}\n")

test_meteorological_data()

