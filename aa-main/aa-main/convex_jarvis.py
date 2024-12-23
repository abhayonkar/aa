def orientation(p, q, r):
    """
    To find the orientation of the ordered triplet (p, q, r).
    The function returns the following values:
    0 --> p, q and r are collinear
    1 --> Clockwise
    2 --> Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def jarvis_march(points):
    """
    Implements the Jarvis March algorithm to find the convex hull of a set of points.
    """
    n = len(points)
    if n < 3:
        return []

    # Initialize the result
    hull = []

    # Find the leftmost point
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i

    # Start from leftmost point, keep moving counterclockwise
    # until reach the start point again.
    p = l
    q = None
    while True:
        # Add current point to result
        hull.append(points[p])

        # Search for a point 'q' such that orientation(p, q, x) is
        # counterclockwise for all points 'x'. The idea is to keep
        # track of the last added point in the result 'hull'. If
        # there is no counterclockwise point with respect to 'p'
        # and 'q', then 'q' is the most counterclockwise point.
        q = (p + 1) % n

        for i in range(n):
            # If i is more counterclockwise than q, then update q
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        # Now q is the most counterclockwise with respect to p.
        # Set p as q for next iteration, so that q is added to
        # result 'hull'
        p = q

        # While we don't come to first point
        if p == l:
            break

    return hull

# Example usage
points = [(0, 0), (1, 1), (2, 2), (2, 0), (2, 4), (3, 3), (4, 2)]
hull = jarvis_march(points)
print("The convex hull is:")
for point in hull:
    print(point)
