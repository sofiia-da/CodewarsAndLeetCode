from collections import deque

def tree_by_levels(node):
    if node is None:
        return []

    result = []
    queue = deque([node])

    while queue:
        current = queue.popleft()
        result.append(current.value)

        #if there's a left child, add it to the back of the queue
        if current.left:
            queue.append(current.left)

        #if there's a right child, add it to the back of the queue
        if current.right:
            queue.append(current.right)

    return result
