from typing import List
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


def read_line() -> str:
    return input_().strip()


def read_int() -> int:
    return int(read_line())


def read_strings() -> List[str]:
    return list(read_line().split())


def read_ints():
    return list(map(int, read_line().split()))


def distance_to_center(x, y):
    return x ** 2 + y ** 2


def get_stones_in_house(rs, rh, stones):
    in_house = []
    for x, y in stones:
        distance = distance_to_center(x, y)
        if (rs + rh) ** 2 >= distance:
            in_house.append(distance)
    return in_house


def get_score(dists1, dists2):
    score = 0
    for dist in dists1:
        is_closest = True
        for dist2 in dists2:
            if dist2 < dist:
                is_closest = False
        score += is_closest
    return score


def solve():
    t = read_int()

    for test in range(1, t + 1):
        rs, rh = read_ints()
        n = read_int()
        red_team = []
        for _ in range(n):
            x, y = read_ints()
            red_team.append((x, y))
        m = read_int()
        yellow_team = []
        for _ in range(m):
            w, z = read_ints()
            yellow_team.append((w, z))

        red_house = get_stones_in_house(rs, rh, red_team)
        yellow_house = get_stones_in_house(rs, rh, yellow_team)

        red, yellow = get_score(red_house, yellow_house), get_score(yellow_house, red_house)
        print_(f"Case #{test}: {red} {yellow}\n")


if __name__ == '__main__':
    solve()
