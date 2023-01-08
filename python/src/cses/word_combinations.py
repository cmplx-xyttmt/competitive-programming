import sys

input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(1000000)
MOD = int(1e9) + 7


class TrieNode:

    def __init__(self):
        self.is_word = False
        self.edges = dict()


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.edges:
                node.edges[c] = TrieNode()
            node = node.edges[c]
        node.is_word = True

    def ways_to_create(self, word):
        cache = [0 for _ in range(len(word) + 1)]

        for index in range(len(word) - 1, -1, -1):
            node = self.root
            j = index
            for i in range(index, len(word)):
                if word[i] not in node.edges:
                    break
                node = node.edges[word[i]]
                if node.is_word:
                    cache[index] = (cache[index] + cache[i + 1]) % MOD
                j += 1
            if node.is_word and j == len(word):
                cache[index] = (cache[index] + 1) % MOD
        return cache[0]


if __name__ == '__main__':
    string = input().strip()
    k = int(input().strip())
    trie = Trie()
    for _ in range(k):
        s = input().strip()
        trie.insert(s)

    print(f"{trie.ways_to_create(string)}\n")
