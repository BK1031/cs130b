import math
import sys

def closest_pair(points):
    if len(points) == 1:
        return ((-sys.maxsize, -sys.maxsize), (sys.maxsize, sys.maxsize))

    if len(points) == 2:
        return points[0], points[1]

    if len(points) == 3:
        return brute_force(points)

    points.sort()

    mid = len(points) // 2
    left_points = points[:mid]
    right_points = points[mid + 1:]

    pair1 = closest_pair(left_points)
    pair2 = closest_pair(right_points)
    dist1 = dist(pair1[0], pair1[1])
    dist2 = dist(pair2[0], pair2[1])

    if dist1 < dist2:
        dist = dist1
        which_pair = 1
    else:
        dist = dist2
        which_pair = 2

    line_points = [point for point in points if abs(point[0] - points[mid][0]) < dist]
    line_points.sort(key=lambda x: x[1])

    pair3 = closest_pair_in_line(line_points, dist)
    dist3 = dist(pair3[0], pair3[1])

    if dist3 < dist:
        dist = dist3
        which_pair = 3

    if which_pair == 1:
        return pair1
    if which_pair == 2:
        return pair2
    if which_pair == 3:
        return pair3

def closest_pair_in_line(points, dist):
    pair3 = ((-sys.maxsize, -sys.maxsize), (sys.maxsize, sys.maxsize))
    min_dist = dist

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if points[j][1] - points[i][1] < min_dist:
                if dist(points[j], points[i]) < min_dist:
                    pair3 = points[j], points[i]
                    min_dist = dist(points[j], points[i])

    return pair3

def dist(a, b):
    dist_x = a[0] - b[0]
    dist_y = a[1] - b[1]
    return math.sqrt(dist_x * dist_x + dist_y * dist_y)

def brute_force(points):
    pair3 = ((-sys.maxsize, -sys.maxsize), (sys.maxsize, sys.maxsize))
    min_dist = dist(pair3[0], pair3[1])

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if dist(points[j], points[i]) < min_dist:
                pair3 = points[j], points[i]
                min_dist = dist(points[j], points[i])

    return pair3


while True:
    n = int(input())
    if n == 0:
        exit()

    points = []
    for _ in range(n):
        x, y = map(float, input().split())
        points.append((x, y))

    res = closest_pair(points)
    print("{:.4f} {:.4f} {:.4f} {:.4f}".format(res[0][0], res[0][1], res[1][0], res[1][1]))