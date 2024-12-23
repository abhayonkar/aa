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














### **13. Convex Hull (Graham’s Scan)**

# #### **Aim**  
# To find the convex hull of a set of points.

# #### **Working**  
# The points are sorted by polar angle, and the hull is constructed using a stack to maintain the counterclockwise order.

# #### **Pseudo Code**  
# ```  
# Algorithm: Graham’s Scan  
# Input: Set of points P  
# Output: Convex hull  

# 1. Sort points by x-coordinate, then by polar angle with respect to the lowest point  
# 2. Initialize an empty stack  
# 3. Push the first three points onto the stack  
# 4. for each remaining point p do  
# 5.     while the top two points and p do not form a counterclockwise turn do  
# 6.         Pop the top point from the stack  
# 7.     Push p onto the stack  
# 8. Return the stack  
# ```

# #### **Complexity and Recurrence Formula**  
# - **Time Complexity**: \(O(n \log n)\)  
# - **Space Complexity**: \(O(n)\)  

# #### **Conclusion**  
# Graham’s Scan is an efficient algorithm for computing convex hulls in 2D.
