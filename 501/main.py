# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def search(self, node: TreeNode | None, counter) -> None:
        if not node:
            return

        if node.left:
            self.search(node.left, counter)

        if node.right:
            self.search(node.right, counter)

        counter[node.val] += 1

    def findMode(self, root: TreeNode | None) -> list[int]:
        counter = defaultdict(lambda: 0)
        self.search(root, counter)
        most_val = max(counter.values())
        return [k for k, v in counter.items() if v == most_val]
