from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []

        columns = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            columns[column].append(node.val)

            if node.left:
                queue.append((node.left, column - 1))

            if node.right:
                queue.append((node.right, column + 1))

        return [columns[column] for column in sorted(columns)]
