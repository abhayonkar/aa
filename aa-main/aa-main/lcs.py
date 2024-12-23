
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Example Input
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS:", lcs(X, Y))























### **2. Longest Common Subsequence (LCS)**

# #### **Aim**  
# To find the longest sequence that appears as a subsequence in two given strings.

# #### **Working**  
# The algorithm builds a table of solutions for subproblems involving prefixes of the input strings. It decides whether to include a character in the LCS by comparing characters of both strings.

# #### **Pseudo Code**  
# ```  
# Algorithm: LCS  
# Input: Strings X of length m, Y of length n  
# Output: Length of LCS  

# 1. Initialize DP table DP[m+1][n+1] to 0  
# 2. for i = 1 to m do  
# 3.     for j = 1 to n do  
# 4.         if X[i-1] == Y[j-1] then  
# 5.             DP[i][j] = DP[i-1][j-1] + 1  
# 6.         else  
# 7.             DP[i][j] = max(DP[i-1][j], DP[i][j-1])  
# 8. Return DP[m][n]  
# ```

# #### **Complexity and Recurrence Formula**  
# - **Time Complexity**: \(O(m \cdot n)\)  
# - **Space Complexity**: \(O(m \cdot n)\)  
# - **Recurrence Relation**:  
#   \(DP[i][j] = \max(DP[i-1][j], DP[i][j-1]) \text{ if } X[i-1] \neq Y[j-1]\)  
#   \(DP[i][j] = 1 + DP[i-1][j-1] \text{ if } X[i-1] == Y[j-1]\)

# #### **Conclusion**  
# The LCS algorithm is an effective solution for sequence comparison and has applications in bioinformatics, text comparison, and version control systems.

# ---