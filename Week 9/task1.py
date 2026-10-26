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


class Queue:
    def __init__(self):
        self.items = []
        self.front = 0
        self.back = 0

    def enqueue(self, value):
        self.items.append(value)
        self.back += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        value = self.items[self.front]
        self.front += 1
        return value

    def is_empty(self):
        return self.front == self.back

    def contents(self):
        return self.items[self.front:self.back]


def bfs(graph, start):
    if start not in graph:
        raise ValueError('Start node is not in the graph')
    queue = Queue()
    queue.enqueue(start)
    dist = {start: 0}
    parent = {start: None}
    order = []
    trace = [(None, [start], queue.contents())]
    while not queue.is_empty():
        u = queue.dequeue()
        order.append(u)
        added = []
        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.enqueue(v)
                added.append(v)
        trace.append((u, added, queue.contents()))
    return order, dist, parent, trace


def rebuild_path(parent, target):
    if target not in parent:
        return []
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path


def shortest_line(graph, start, target):
    _, dist, parent, _ = bfs(graph, start)
    path = rebuild_path(parent, target)
    if not path:
        return f'Shortest {start} -> {target}: no path'
    return (f'Shortest {start} -> {target}: distance {dist[target]}, path '
            + ' -> '.join(path))


def main():
    order, _, _, _ = bfs(GRAPH, 'A')
    print('BFS order from A: ' + ' '.join(order))
    print(shortest_line(GRAPH, 'A', 'G'))
    print(shortest_line(GRAPH, 'D', 'G'))


if __name__ == '__main__':
    main()
