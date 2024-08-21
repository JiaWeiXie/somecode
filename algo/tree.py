class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


data = [1, 2, 3, 4, 5, 6, 7]


def init_tree(data: list[int]) -> TreeNode:
    nodes = [TreeNode(val) for val in data]
    for i, node in enumerate(nodes):
        if node is None:
            continue
        if 2 * i + 1 < len(nodes):
            node.left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            node.right = nodes[2 * i + 2]
    return nodes[0]


def bfs(root: TreeNode) -> None:
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def dfs_preorder(node: TreeNode | None) -> None:
    if node is None:
        return
    print(node.val)
    dfs_preorder(node.left)
    dfs_preorder(node.right)


def dfs_inorder(node: TreeNode | None) -> None:
    if node is None:
        return
    dfs_inorder(node.left)
    print(node.val)
    dfs_inorder(node.right)


def dfs_postorder(node: TreeNode | None) -> None:
    if node is None:
        return
    dfs_postorder(node.left)
    dfs_postorder(node.right)


if __name__ == "__main__":
    root = init_tree(data)
    # bfs(root)
    # dfs_preorder(root)
    # dfs_inorder(root)
    dfs_postorder(root)
