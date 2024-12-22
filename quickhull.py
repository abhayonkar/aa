def quickhull(points):
    if len(points) < 3:
        return points

    def find_side(p1, p2, p):
        return (p[0] - p1[0]) * (p2[1] - p1[1]) - (p[1] - p1[1]) * (p2[0] - p1[0])

    def distance(p1, p2, p):
        return abs((p[0] - p1[0]) * (p2[1] - p1[1]) - (p[1] - p1[1]) * (p2[0] - p1[0]))

    def find_hull(p1, p2, points, hull):
        if not points:
            return

        farthest_point = max(points, key=lambda p: distance(p1, p2, p))
        hull.append(farthest_point)

        left_set = [p for p in points if find_side(p1, farthest_point, p) > 0]
        right_set = [p for p in points if find_side(farthest_point, p2, p) > 0]

        find_hull(p1, farthest_point, left_set, hull)
        find_hull(farthest_point, p2, right_set, hull)

    min_point = min(points, key=lambda p: p[0])
    max_point = max(points, key=lambda p: p[0])

    hull = [min_point, max_point]

    left_of_line = [p for p in points if find_side(min_point, max_point, p) > 0]
    right_of_line = [p for p in points if find_side(max_point, min_point, p) > 0]

    find_hull(min_point, max_point, left_of_line, hull)
    find_hull(max_point, min_point, right_of_line, hull)

    return hull

if __name__ == "__main__":
    points = [(0, 0), (1, 1), (2, 2), (2, 0), (2, 4), (3, 3), (0, 3)]
    hull_points = quickhull(points)

    # Print the points forming the smallest convex polygon
    print("Abhay Onkar")
    print("Points forming the convex hull:")
    output = []
    for point in sorted(hull_points):
        output.append(point)

    print(output)
