import math


def is_angle_obtuse(x, y, z):
    return math.acos((y ** 2 + z ** 2 - x ** 2) / (2 * y * z)) - math.pi / 2 > 1e-6


def is_obtuse(x, y, z):
    if x < y:
        x, y = y, x
    if x < z:
        x, z = z, x
    return is_angle_obtuse(x, y, z)


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def is_linear(x1, y1, x2, y2, x3, y3):
    return (x1 - x2) * (y1 - y3) == (x1 - x3) * (y1 - y2)


def check_neighbors(x1, y1, x2, y2, n, m):
    x = distance(x1, y1, x2, y2)
    for x3 in range(x1 - 1, x1 + 2):
        for y3 in range(y1 - 1, y1 + 2):
            if x1 == x3 and y1 == y3:
                continue
            if 0 <= x3 < n and 0 <= y3 < m and not is_linear(x1, y1, x2, y2, x3, y3):
                y = distance(x1, y1, x3, y3)
                z = distance(x2, y2, x3, y3)
                if is_obtuse(x, y, z):
                    return x3, y3
    return None


def find_point(x1, y1, x2, y2, n, m):
    point = check_neighbors(x1, y1, x2, y2, n, m)
    if point:
        return point
    return check_neighbors(x2, y2, x1, y1, n, m)


if __name__ == '__main__':
    _n, _m = map(int, input().split())
    _x1, _y1, _x2, _y2 = map(int, input().split())
    ans = find_point(_x1, _y1, _x2, _y2, _n, _m)
    print(ans[0], ans[1])
