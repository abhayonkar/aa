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


# t - O(n*2)
# s - O(n*2)