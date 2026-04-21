# Pre-order traversal: Root -> Left -> Right
def pre_order(node):
    if node is None:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)

# In-order traversal: Left -> Root -> Right
def in_order(node):
    if node is None:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)

# Post-order traversal: Left -> Right -> Root
def post_order(node):
    if node is None:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]
