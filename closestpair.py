import math


def closest_pair(P):
    if len(P) <= 3:
        return brute_force(P)

    mid = len(P) // 2
    Q = P[:mid]
    R = P[mid:]

    d1, pair1 = closest_pair(Q)
    d2, pair2 = closest_pair(R)

    if d1 < d2:
        d, current_closest_pair = d1, pair1
    else:
        d, current_closest_pair = d2, pair2

    strip = [p for p in P if abs(p[0] - P[mid][0]) < d]
    strip_d, strip_pair = strip_closest(strip, d)

    if strip_d < d:
        return strip_d, strip_pair
    return d, current_closest_pair


def strip_closest(strip, d):
    min_dist = d
    closest_pair = None
    length = len(strip)

    for i in range(length):
        for j in range(i + 1, min(i + 7, length)):
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (strip[i], strip[j])
    return min_dist, closest_pair


def brute_force(P):
    min_dist = float('inf')
    closest_pair = None
    length = len(P)

    for i in range(length):
        for j in range(i + 1, length):
            dist = distance(P[i], P[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (P[i], P[j])
    return min_dist, closest_pair


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Example usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
points.sort()
distance, closest_points = closest_pair(points)
print("Abhay Onkar")
print("The smallest distance is", distance)
print("The closest pair of points is", closest_points)
