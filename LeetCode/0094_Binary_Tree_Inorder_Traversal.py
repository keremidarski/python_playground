# Problem description:
# https://leetcode.com/problems/binary-tree-inorder-traversal/

def inorder_traversal(root):
    res, stack = [], [(root, False)]

    while stack:
        node, visited = stack.pop()  # the last element

        if node:
            if visited:
                res.append(node.val)
            else:  # inorder: left -> root -> right
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))

    return res


# Expected: [1, 3, 2]
print(inorder_traversal([1, None, 2, 3]))
# Expected: []
print(inorder_traversal([]))
# Expected: [1]
print(inorder_traversal([1]))