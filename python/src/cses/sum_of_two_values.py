from typing import Tuple, Optional

if __name__ == '__main__':
    n, x = map(int, input().split(" "))

    a = list(map(int, input().split(" ")))

    num_to_index = dict()
    ans: Optional[Tuple[int, int]] = None
    for i in range(n):
        diff = x - a[i]
        if diff in num_to_index:
            ans = (num_to_index[diff], i)
            break
        num_to_index[a[i]] = i

    if ans:
        print(f"{ans[0] + 1} {ans[1] + 1}")
    else:
        print("IMPOSSIBLE")
