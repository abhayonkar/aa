def knapsack(values, weights, capacity):
    n = len(values)
    # Create a 2D array to store the maximum value at each capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table dp[][] in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # The maximum value that can be put in a knapsack of capacity
    return dp[n][capacity]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = knapsack(values, weights, capacity)
print(f"The maximum value that can be put in a knapsack of capacity {capacity} is {max_value}.")


# O(nW) n = number of valus
# W - weights