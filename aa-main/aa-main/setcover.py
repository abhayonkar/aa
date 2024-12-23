def set_cover(universe, subsets):
    
    # Initialize the covered set and the result list
    covered = set()
    result = []

    # While there are still elements to cover
    while covered != universe:
        # Find the subset that covers the most uncovered elements
        best_subset = None
        best_subset_coverage = set()

        for subset in subsets:
            coverage = subset & (universe - covered)
            if len(coverage) > len(best_subset_coverage):
                best_subset = subset
                best_subset_coverage = coverage

        # Add the best subset to the result and update the covered set
        covered |= best_subset
        result.append(best_subset)

    return result

# Example usage
universe = set(range(1, 11))  # {1, 2, 3, ..., 10}
subsets = [
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
    {1, 2, 10},
    {3, 4, 5},
    {6, 7, 8},
    {9, 10}
]

cover = set_cover(universe, subsets)
print("Selected subsets for the cover:")
for subset in cover:
    print(subset)










"""
    Greedy algorithm to approximate the Set Cover problem.

    :param universe: The set of elements to be covered.
    :param subsets: A list of subsets of the universe.
    :return: A list of subsets that cover the universe.
    """



### **15. Set Cover Problem**

# #### **Aim**  
# To find the smallest subset of sets that covers all elements.

# #### **Working**  
# The greedy algorithm iteratively picks the set that covers the largest number of uncovered elements.

# #### **Pseudo Code**  
# ```  
# Algorithm: Set Cover (Greedy)  
# Input: Universe U, collection of sets S  
# Output: Subset of S covering U  

# 1. Initialize covered = ∅, result = ∅  
# 2. while covered ≠ U do  
# 3.     Select set S_i ∈ S that maximizes |S_i ∩ (U \ covered)|  
# 4.     Add S_i to result  
# 5.     Update covered = covered ∪ S_i  
# 6. Return result  
# ```

# #### **Complexity and Recurrence Formula**  
# - **Time Complexity**: \(O(n \cdot m)\), where \(n\) is the number of sets and \(m\) is the universe size.  

# #### **Conclusion**  
# The greedy algorithm gives an approximation for the set cover problem with a logarithmic factor.

# ---