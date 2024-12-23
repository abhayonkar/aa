def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Target not found

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 3
result = binary_search(sorted_list, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")




















### **4. Binary Search**

# #### **Aim**  
# To efficiently search for an element in a sorted array.

# #### **Working**  
# The algorithm divides the search range in half at each step by comparing the target element with the middle element of the array.

# #### **Pseudo Code**  
# ```  
# Algorithm: Binary Search  
# Input: Sorted array arr[], element x  
# Output: Index of x or -1 if not found  

# 1. Initialize low = 0, high = n-1  
# 2. while low ≤ high do  
# 3.     mid = (low + high) // 2  
# 4.     if arr[mid] == x then  
# 5.         Return mid  
# 6.     else if arr[mid] > x then  
# 7.         high = mid - 1  
# 8.     else  
# 9.         low = mid + 1  
# 10. Return -1  
# ```

# #### **Complexity and Recurrence Formula**  
# - **Time Complexity**: \(O(log n)\)  
# - **Space Complexity**: \(O(1)\)  
# - **Recurrence Relation**:  
#   \(T(n) = T(n/2) + O(1)\)

# #### **Conclusion**  
# Binary Search is highly efficient for sorted datasets and is a foundational algorithm for divide-and-conquer strategies.

# ---