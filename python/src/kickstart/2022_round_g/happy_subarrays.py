from collections import defaultdict
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


def compress_coordinates(coordinates):
    coordinates = sorted(set(coordinates))
    mapping = dict()
    for i, coord in enumerate(coordinates):
        mapping[coord] = i
    return mapping


def solve():
    t = read_int()
    for test in range(1, t + 1):
        n = read_int()
        a = read_ints()
        pref = [0]
        pref2 = [0]
        for num in a:
            pref.append(pref[-1] + num)
        for i in range(1, n + 1):
            pref2.append(pref[i] + pref2[-1])
        mapping = compress_coordinates(pref)
        pref_to_index = defaultdict(list)
        data = [n + 1] * len(mapping)
        for i in range(1, n + 1):
            p = pref[i]
            pref_to_index[mapping[p]].append(i)
            if data[mapping[p]] == n + 1:
                data[mapping[p]] = i
        for values in pref_to_index.values():
            values.reverse()
        # print(mapping)
        # print(data)
        segment_tree = SegmentTree(data, default=n + 1, func=min)
        ans = 0
        for i in range(1, n + 1):
            rem_i = pref[i - 1]
            j = segment_tree.query(0, mapping[rem_i])
            if pref[i] - pref[i - 1] >= 0:
                ans += pref2[j - 1] - pref2[i - 1] - (j - i) * rem_i
                # print(i, j, pref2[j - 1] - pref2[i - 1] - (j - i) * rem_i)
            p = pref[i]
            mp = pref_to_index[mapping[p]]
            if mp:
                mp.pop()
            update = n + 1 if len(mp) == 0 else mp[-1]
            segment_tree[mapping[p]] = update

        print_(f"Case #{test}: {ans}\n")


if __name__ == '__main__':
    solve()
