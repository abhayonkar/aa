def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example Input
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print("Maximum value:", knapsack(values, weights, capacity))





















# Here’s a streamlined template with the requested sections filled out for multiple algorithms:

# ---

# ### **1. 0/1 Knapsack**

# #### **Aim**  
# To determine the maximum value obtainable by selecting items within a given weight capacity.

# #### **Working**  
# The algorithm solves the problem by breaking it into subproblems, where each subproblem considers whether to include or exclude the current item based on the remaining capacity.

# #### **Pseudo Code**  
# ```  
# Algorithm: 0/1 Knapsack  
# Input: Array values[], weights[], capacity W, number of items n  
# Output: Maximum value that can be obtained

# 1. Initialize DP table DP[n+1][W+1] to 0  
# 2. for i = 1 to n do  
# 3.     for w = 1 to W do  
# 4.         if weights[i-1] ≤ w then  
# 5.             DP[i][w] = max(DP[i-1][w], values[i-1] + DP[i-1][w-weights[i-1]])  
# 6.         else  
# 7.             DP[i][w] = DP[i-1][w]  
# 8. Return DP[n][W]  
# ```

# #### **Complexity and Recurrence Formula**  
# - **Time Complexity**: \(O(n \cdot W)\)  
# - **Space Complexity**: \(O(n \cdot W)\)  
# - **Recurrence Relation**:  
#   \(DP[i][w] = \max(DP[i-1][w], values[i-1] + DP[i-1][w-weights[i-1]])\)

# #### **Conclusion**  
# The 0/1 Knapsack algorithm is efficient for solving bounded optimization problems but becomes computationally expensive for large weight limits.

# ---



