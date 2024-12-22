def polar_angle(p0, p1):
    y_span = p1[1] - p0[1]
    x_span = p1[0] - p0[0]
    return (y_span, x_span)

def distance(p0, p1):
    return (p1[1] - p0[1])**2 + (p1[0] - p0[0])**2

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def graham_scan(points):
    start = min(points, key=lambda p: (p[1], p[0]))
    sorted_points = sorted(points, key=lambda p: polar_angle(start, p))

    hull = [start, sorted_points[0]]

    for s in sorted_points[1:]:
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], s) <= 0:
            hull.pop()
        hull.append(s)

    return hull

# Example usage
points = [(0, 0), (1, 1), (2, 2), (2, 0), (2, 4), (3, 3), (4, 2)]
hull = graham_scan(points)
print("Convex Hull:", hull)
