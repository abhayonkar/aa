from itertools import permutations

def calculate_total_distance(path, distance_matrix):
    total_distance = 0
    num_cities = len(path)
    for i in range(num_cities - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    total_distance += distance_matrix[path[-1]][path[0]]  # Return to the origin city
    return total_distance

def traveling_salesman(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    min_distance = float('inf')
    best_path = None

    # Generate all permutations of cities
    for path in permutations(cities):
        current_distance = calculate_total_distance(path, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = path

    return best_path, min_distance

# Example usage
if __name__ == "__main__":
    # Distance matrix (symmetric)
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    best_path, min_distance = traveling_salesman(distance_matrix)
    print(f"Best path: {best_path}")
    print(f"Minimum distance: {min_distance}")
