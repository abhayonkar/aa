def generate_pascals_triangle(num_rows):
    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, num_rows):
        # Start the previous row with 1
        row = [1]
        # Compute the values in the row
        for j in range(1, i):
            # Each value is the sum of the two values above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End the row with 1
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)))

# Example usage
num_rows = 5
triangle = generate_pascals_triangle(num_rows)
print_pascals_triangle(triangle)










### **12. Pascal’s Triangle**

# #### **Aim**  
# To generate Pascal's Triangle and compute binomial coefficients.

# #### **Working**  
# Each entry is the sum of the two entries directly above it.

# #### **Pseudo Code**  
# ```  
# Algorithm: Pascal’s Triangle  
# Input: Number of rows n  
# Output: Pascal’s Triangle  

# 1. Initialize triangle[0][0] = 1  
# 2. for i = 1 to n do  
# 3.     triangle[i][0] = 1  
# 4.     for j = 1 to i do  
# 5.         triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]  
# 6. Return triangle  
# ```

# #### **Complexity and Recurrence Formula**  
# - **Time Complexity**: \(O(n^2)\)  
# - **Space Complexity**: \(O(n^2)\)  
# - **Recurrence Relation**:  
#   \(C(n, k) = C(n-1, k-1) + C(n-1, k)\)

# #### **Conclusion**  
# Pascal’s Triangle is a simple but fundamental tool in combinatorics and number theory.

# ---