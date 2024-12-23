class Event:
    def __init__(self, x, y, segment, is_start):
        self.x = x
        self.y = y
        self.segment = segment
        self.is_start = is_start

def find_intersections(segments):
    events = []
    for segment in segments:
        (x1, y1), (x2, y2) = segment
        events.append(Event(x1, y1, segment, True))
        events.append(Event(x2, y2, segment, False))

    # Bubble sort to sort events by x-coordinate
    n = len(events)
    for i in range(n):
        for j in range(0, n-i-1):
            if events[j].x > events[j+1].x:
                events[j], events[j+1] = events[j+1], events[j]

    active_segments = []
    intersections = []

    for event in events:
        if event.is_start:
            for active in active_segments:
                if intersect(event.segment, active):
                    intersections.append(find_intersection_point(event.segment, active))
            active_segments.append(event.segment)
        else:
            active_segments.remove(event.segment)

    return intersections

def intersect(seg1, seg2):
    (x1, y1), (x2, y2) = seg1
    (x3, y3), (x4, y4) = seg2
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    o1 = orientation((x1, y1), (x2, y2), (x3, y3))
    o2 = orientation((x1, y1), (x2, y2), (x4, y4))
    o3 = orientation((x3, y3), (x4, y4), (x1, y1))
    o4 = orientation((x3, y3), (x4, y4), (x2, y2))

    if o1 != o2 and o3 != o4:
        return True
    return False

def find_intersection_point(seg1, seg2):
    (x1, y1), (x2, y2) = seg1
    (x3, y3), (x4, y4) = seg2
    a1 = y2 - y1
    b1 = x1 - x2
    c1 = a1 * x1 + b1 * y1
    a2 = y4 - y3
    b2 = x3 - x4
    c2 = a2 * x3 + b2 * y3
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None
    else:
        x = (b2 * c1 - b1 * c2) / det
        y = (a1 * c2 - a2 * c1) / det
        return (x, y)

# Example usage
segments = [
    ((1, 1), (4, 3)),
    ((1, 4), (4, 1)),
    ((2, 2), (3, 3))
]

intersections = find_intersections(segments)
print("Intersections:", intersections)















### **11. Sweep Line Algorithm**

# #### **Aim**  
# To solve geometric problems like finding intersections or handling events in a sorted manner using a sweep line.

# #### **Working**  
# The algorithm processes events in sorted order along one dimension, maintaining active intervals or points in a balanced structure.

# #### **Pseudo Code**  
# ```  
# Algorithm: Sweep Line  
# Input: Set of events (e.g., line segments)  
# Output: Processed events or intersections  

# 1. Sort events by x-coordinate  
# 2. Initialize an empty active set  
# 3. for each event in sorted events do  
# 4.     if event is a start point then  
# 5.         Add it to the active set  
# 6.     if event is an end point then  
# 7.         Remove it from the active set  
# 8.     Check for intersections in the active set  
# 9. Return results  
# ```

# #### **Complexity and Recurrence Formula**  
# - **Time Complexity**: \(O(n \log n)\)  
# - **Space Complexity**: \(O(n)\)  

# #### **Conclusion**  
# The sweep line algorithm is efficient for solving intersection problems in computational geometry.