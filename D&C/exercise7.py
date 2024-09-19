from math import dist
points = [(2, 1), (-4, 5), (10, 0), (1, 2), (4, 4), (1, 1), (2, 2)]
#points = [(-4, 5), (1, 2), (2, 1)]
#points.sort(key=lambda x: x[0])

#print(points)
def brute_force_closest_points(points):
    min_dist = float('inf')
    pair = (None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair

def closest_points(points):
    px = points.copy()
    py = points.copy()
    px.sort(key=lambda p: p[0]) # O(n log n)
    py.sort(key=lambda p: p[1]) # O(n log n)
    [x, y] = _closest_points(px, py)
    print(dist(x,y))
    return [x, y]

def _closest_points(px, py):
    if len(px) <= 3:
        return brute_force_closest_points(px)
    
    # Dividimos los puntos en dos mitades
    mid = len(px) // 2
    mid_point = px[mid]
    
    qx = px[:mid] # O(n)
    qy = list(filter(lambda p: p[0] <= mid_point[0], py)) # O(n)
    rx = px[mid:] # O(n)
    ry = list(filter(lambda p: p[0] > mid_point[0], py)) # O(n)

    q0, q1 = _closest_points(qx, qy)
    r0, r1 = _closest_points(rx, ry)

    d = min(dist(q0, q1), dist(r0, r1))

    sy = list(filter(lambda p: abs(p[0] - mid_point[0]) <= d, py))

    s0 = q0
    s1 = q1

    for i in range(len(sy)): # O(n)
        for j in range(i + 1, i + 15): # O(15) -> O(1)
            if (j >= len(sy)):
                break
            if dist(sy[i], sy[j]) < d:
                s0 = sy[i]
                s1 = sy[j]

    if dist(s0, s1) < d:
        return (s0, s1)
    if dist(q0, q1) < dist(r0, r1):
        return (q0, q1)
    return (r0, r1)

    





def main():
    print(closest_points(points))

if __name__ == '__main__':
    main()
