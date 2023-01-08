class Adventurer:

    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = int(s1)
        self.s2 = int(s2)
        self.s3 = int(s3)


if __name__ == '__main__':
    n = int(input())
    adventurers = []
    for _ in range(n):
        name, s1, s2, s3 = input().split()
        adventurers.append(Adventurer(name, s1, s2, s3))

    adventurers.sort(key=lambda x: x.name)
    skill_1 = sorted(adventurers, key=lambda x: x.s1, reverse=True)
    skill_2 = sorted(adventurers, key=lambda x: x.s2, reverse=True)
    skill_3 = sorted(adventurers, key=lambda x: x.s3, reverse=True)

    adv_lists = [skill_1, skill_2, skill_3]
    indices = [0, 0, 0]

    seen = set()
    team = []
    while all(map(lambda x: x < n, indices)):
        index = len(team)
        while indices[index] < n and adv_lists[index][indices[index]].name in seen:
            indices[index] += 1
        if indices[index] < n:
            adv = adv_lists[index][indices[index]]
            team.append(adv.name)
            seen.add(adv.name)
            if len(team) == 3:
                team.sort()
                print(" ".join(team))
                team = []
