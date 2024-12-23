def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)



















### **5. Quick Sort**

# #### **Aim**  
# To sort an array using the divide-and-conquer paradigm.

# #### **Working**  
# The array is partitioned around a pivot, placing smaller elements to its left and larger to its right. This process is recursively applied to the partitions.

# #### **Pseudo Code**  
 
# Algorithm: Quick Sort  
# Input: Array arr[], low, high  
# Output: Sorted array  

# 1. if low < high then  
# 2.     pivot = partition(arr, low, high)  
# 3.     quickSort(arr, low, pivot-1)  
# 4.     quickSort(arr, pivot+1, high)  

# Partition(arr, low, high):  
# 1. Set pivot = arr[high], i = low-1  
# 2. for j = low to high-1 do  
# 3.     if arr[j] < pivot then  
# 4.         i = i + 1  
# 5.         Swap arr[i] and arr[j]  
# 6. Swap arr[i+1] and arr[high]  
# 7. Return i+1  


# #### **Complexity and Recurrence Formula**  
# - **Best/Average Time Complexity**: \(O(n \log n)\)  
# - **Worst Time Complexity**: \(O(n^2)\)  
# - **Space Complexity**: \(O(\log n)\) (for recursion)  
# - **Recurrence Relation**:  
#   \(T(n) = T(k) + T(n-k-1) + O(n)\), where \(k\) is the partition index.

# #### **Conclusion**  
# Quick Sort is one of the fastest sorting algorithms for general-purpose use but performs poorly on already sorted or nearly sorted data without optimizations.