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
    print("pritam rote")
    print("Points forming the convex hull:")
    output = []
    for point in sorted(hull_points):
        output.append(point)

    print(output)

















# ### **Quick Hull Algorithm**

# #### **Aim**  
# To find the convex hull of a set of points in 2D space using a divide-and-conquer approach.

# ---

# #### **Working**  
# Quick Hull finds the convex hull by dividing the set of points into subsets based on their relation to the line formed by the leftmost and rightmost points. It recursively finds points that form the convex hull.

# Steps:  
# 1. Find the leftmost and rightmost points (extreme points) to form a base line.  
# 2. Divide the set of points into two subsets, above and below the base line.  
# 3. For each subset, find the farthest point from the line.  
# 4. Add this point to the hull and repeat the process for the lines formed by the farthest point and the two endpoints of the line.  
# 5. Stop when no points are outside the line segments.

# ---

# #### **Pseudo Code**  
# ```  
# Algorithm: Quick Hull  
# Input: Set of points P  
# Output: Points forming the convex hull  

# 1. Find the leftmost (min_x) and rightmost (max_x) points in P  
# 2. Add min_x and max_x to the hull  
# 3. Divide P into two subsets:  
#      a. Points above the line min_x → max_x  
#      b. Points below the line min_x → max_x  
# 4. FindHull(P_above, min_x, max_x)  
# 5. FindHull(P_below, max_x, min_x)  

# FindHull(S, P1, P2):  
# 1. if S is empty then  
# 2.     Return  
# 3. Find the farthest point P_far from the line P1 → P2  
# 4. Add P_far to the hull  
# 5. Divide S into subsets:  
#      a. Points above P1 → P_far  
#      b. Points above P_far → P2  
# 6. Recursively call FindHull on these subsets  
# ```

# ---

# #### **Complexity and Recurrence Formula**  
# - **Time Complexity**:  
#   - Best/Average Case: \(O(n \log n)\)  
#   - Worst Case: \(O(n^2)\) (for degenerate cases like collinear points)  
# - **Space Complexity**: \(O(n)\) (for recursion stack)  

# **Recurrence Relation**:  
# \(T(n) = 2T(n/2) + O(n)\), where \(n\) is the number of points.

# ---

# #### **Conclusion**  
# Quick Hull is a faster alternative to some other convex hull algorithms (e.g., Jarvis's March) in practice, especially for random input, but it may perform poorly for degenerate or pathological cases.