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


def solve():
    t = read_int()
    for _ in range(t):
        n = read_int()
        a = read_ints()
        left_bound = []
        right_bound = []
        left = []
        for i, ai in enumerate(a):
            while left and ai >= a[left[-1]]:
                left.pop()
            if left:
                left_bound.append(left[-1])
            else:
                left_bound.append(-1)
            left.append(i)

        right = []
        for i in range(n - 1, -1, -1):
            while right and a[i] >= a[right[-1]]:
                right.pop()
            if right:
                right_bound.append(right[-1])
            else:
                right_bound.append(n)
            right.append(i)

        right_bound.reverse()

        a_prefix = [a[0]]
        for i in range(1, n):
            a_prefix.append(a_prefix[-1] + a[i])
        # print("Prefix: ", a_prefix)

        min_seg = SegmentTree(a_prefix, int(1e18) + 1, min)
        max_seg = SegmentTree(a_prefix, -int(1e18) - 1, max)
        holds = True
        for i in range(n):
            min_left = min_seg.query(max(0, left_bound[i]), i) if i > 0 else 0
            if left_bound[i] == -1:
                min_left = min(0, min_left)
            max_right = max_seg.query(i, right_bound[i])
            # print(f"Bounds: {left_bound[i]} {i} {right_bound[i]}")
            # print(a[i], min_left, max_right, f" -> {a[i]} vs {(max_right - min_left)}")
            holds = a[i] >= (max_right - min_left)
            if not holds:
                break

        print_(f"{'YES' if holds else 'NO'}\n")


if __name__ == '__main__':
    solve()
