n = input()

def is_subsequence(num: str):
    start, end = 0, len(n)
    for c in num:
        f = n.find(c, start, end)
        if f == -1:
            return False
        start = f + 1
    return True

print(is_subsequence(str(128)))

# found = False
# for num in range(0, 1000, 8):
#     if is_subsequence(str(num)):
#         print(num)
#         found = True
#         break
#
# if not found:
#     print(-1)
