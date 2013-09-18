

def bfs(root, callback):
    queue = [root]
    while queue:
        # Get the next element
        current = queue.pop(0)
        # Callback
        callback(current)
        # Add children to queue
        queue.extend(current.children)
