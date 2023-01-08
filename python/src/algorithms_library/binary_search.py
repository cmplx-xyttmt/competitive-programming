from typing import Callable


def find_first_false(l_: int, r: int, f: Callable[[int], bool]):
    """
    The binary search function below returns the first value x for which f(x) = false.
    [l, r] is the range of integers to search
    f is the predicate function which satisfies the following property: there exists an
    integer t such that for all l <= x < t, f(x) is true, and for all t <= x <= r, f(x)
    is false.

    Based on this blog: https://codeforces.com/blog/entry/96699
    """
    l_, r = l_ - 1, r + 1
    while r - l_ > 1:
        m = l_ + (r - l_) // 2
        if f(m):
            l_ = m
        else:
            r = m

    return r


if __name__ == '__main__':
    # Example usage of the above to find position of element x in list a (or its insertion point if it doesn't exist)
    a = [1, 2, 2, 3, 4, 6, 6, 7, 8]
    n = len(a)
    search_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in search_values:
        pos = find_first_false(0, n - 1, lambda i: a[i] < x)
        print(x, pos)
