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
print("pritam rote")
print("The smallest distance is", distance)
print("The closest pair of points is", closest_points)








### **6. Closest Pair of Points**

# #### **Aim**  
# To find the closest pair of points in a 2D plane.

# #### **Working**  
# The points are divided into two halves. The closest pairs are found recursively in both halves and across the dividing line.

# #### **Pseudo Code**  
# ```  
# Algorithm: Closest Pair of Points  
# Input: Set of points P  
# Output: Pair of points with minimum distance  

# 1. Sort points by x-coordinate  
# 2. Divide points into two halves, PL and PR  
# 3. Recursively find closest pairs in PL and PR  
# 4. Find closest pair across the dividing line  
# 5. Return the smallest distance  
# ```

# #### **Complexity and Recurrence Formula**  
# - **Time Complexity**: \(O(n \log n)\)  
# - **Space Complexity**: \(O(n)\)  
# - **Recurrence Relation**:  
#   \(T(n) = 2T(n/2) + O(n)\)

# #### **Conclusion**  
# Efficiently solves geometric problems by reducing the search space using divide-and-conquer.
