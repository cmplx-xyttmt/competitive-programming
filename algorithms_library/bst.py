from typing import Optional


class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.size = 0


class BST:

    def __init__(self):
        self._root = None

    def _get(self, x: Optional[Node], key):
        if x is None:
            raise KeyError
        if key < x.key:
            return self._get(x.left, key)
        elif x.key < key:
            return self._get(x.right, key)
        else:
            return x.val

    def __getitem__(self, key):
        return self._get(self._root, key)

    @staticmethod
    def size(x: Optional[Node]):
        if not x:
            return 0
        return x.size

    def _set(self, x: Optional[Node], key, val):
        if x is None:
            return Node(key, val)
        if key < x.key:
            x.left = self._set(x.left, key, val)
        elif x.key < key:
            x.right = self._set(x.right, key, val)
        else:
            x.val = val
        x.size = self.size(x.left) + self.size(x.right) + 1
        return x

    def __setitem__(self, key, value):
        self._root = self._set(self._root, key, value)

    def min(self):
        return self._min(self._root).key

    def _min(self, x: Optional[Node]):
        if not x.left:
            return x
        return self._min(x.left)

    def floor(self, key):
        x = self._floor(self._root, key)
        if not x:
            return None
        return x.key

    def _floor(self, x: Optional[Node], key):
        if not x:
            return None
        if x.key == key:
            return x
        if key < x.key:
            return self._floor(x.left, key)
        t = self._floor(x.right, key)
        if t:
            return t
        return x

    def select(self, k):
        # Finds the node with the key ky such that there are k nodes with key < ky. i.e the (k - 1)th node.
        # Returns the key of the node
        return self._select(self._root, k).key

    def _select(self, x: Optional[Node], k):
        if not x:
            return None
        t = self.size(x.left)
        if t > k:
            return self._select(x.left, k)
        elif t == k:
            return x
        else:
            return self._select(x.right, k - t - 1)

    def rank(self, k):
        # returns number of keys less than k
        return self._rank(self._root, k)

    def _rank(self, x: Optional[Node], k):
        # Returns number of keys less than k in the subtree rooted at x.
        if not x:
            return 0
        if k < x.key:
            return self._rank(x.left, k)
        elif k == x.key:
            return self.size(x.left)
        else:
            return 1 + self.size(x.left) + self._rank(k, x.right)

    def delete_min(self):
        self._root = self._delete_min(self._root)

    def _delete_min(self, x: Optional[Node]):
        if not x:
            return None
        if x.left:
            x.left = self._delete_min(x.left)
            x.size = 1 + self.size(x.left) + self.size(x.right)
            return x
        else:
            return x.right

    def delete(self, k):
        # Delete node with key k
        self._root = self._delete(self._root, k)

    def _delete(self, x: Optional[Node], k) -> Optional[Node]:
        if not x:
            return None
        if k < x.key:
            x.left = self._delete(x.left, k)
        elif k > x.key:
            x.right = self._delete(x.right, k)
        else:
            if not x.left:
                return x.right
            if not x.right:
                return x.left
            t = x
            x = self._min(t.right)
            x.right = self._delete_min(t.right)
            x.left = t.left
        x.size = 1 + self.size(x.left) + self.size(x.right)
        return x
