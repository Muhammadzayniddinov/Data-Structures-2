# Muhammad Zayniddinov

GRAPH = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F'],
}


class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, value):
        self.items.append(value)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        value = self.items.pop()
        self.top -= 1
        return value

    def is_empty(self):
        return self.top == -1

    def contents(self):
        return self.items[::-1]


def dfs(graph, start):
    if start not in graph:
        raise ValueError('Start node is not in the graph')
    stack = Stack()
    stack.push(start)
    visited = set()
    order = []
    trace = [(None, 'Initialize', [start], stack.contents())]
    while not stack.is_empty():
        u = stack.pop()
        if u in visited:
            trace.append((u, 'Skip visited', [], stack.contents()))
            continue
        visited.add(u)
        order.append(u)
        pushed = []
        for v in reversed(graph[u]):
            if v not in visited:
                stack.push(v)
                pushed.append(v)
        trace.append((u, 'Visit', pushed, stack.contents()))
    return order, trace


def main():
    for start in ['A', 'G']:
        order, _ = dfs(GRAPH, start)
        print(f'DFS order from {start}: ' + ' '.join(order))


if __name__ == '__main__':
    main()
