import random

print(1)
n = 200000
m = int(1e18)
nums = []
for _ in range(n):
    nums.append(random.choice(range(1, int(1e9))))

string = " ".join(map(str, nums))
print(f"{n} {m}")
print(string)
