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
