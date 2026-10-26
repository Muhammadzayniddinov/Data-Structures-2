# Muhammad Zayniddinov

GRAPH = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
    'E': [('C', 10), ('D', 2), ('F', 3)],
    'F': [('D', 6), ('E', 3)],
}
INF = float('inf')


def dijkstra(graph, source):
    if source not in graph:
        raise ValueError('Source node is not in the graph')
    if any(weight < 0 for edges in graph.values() for _, weight in edges):
        raise ValueError('Dijkstra requires non-negative weights')
    nodes = sorted(graph)
    dist = {node: INF for node in nodes}
    prev = {node: None for node in nodes}
    dist[source] = 0
    settled = set()
    states = [('init', dist.copy())]
    trace = []
    while len(settled) < len(nodes):
        u = None
        for node in nodes:
            if node not in settled and (u is None or dist[node] < dist[u]):
                u = node
        if u is None or dist[u] == INF:
            break
        settled.add(u)
        updates = []
        for v, weight in sorted(graph[u]):
            if v not in settled:
                candidate = dist[u] + weight
                if candidate < dist[v]:
                    dist[v] = candidate
                    prev[v] = u
                    updates.append((v, candidate, u))
        trace.append((u, dist[u], updates))
        states.append((f'settle {u} ({dist[u]})', dist.copy()))
    return dist, prev, states, trace


def rebuild_path(prev, dist, target):
    if target not in dist or dist[target] == INF:
        return []
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    return path


def format_states(states):
    lines = []
    for label, dist in states:
        values = ' '.join(f'{v}={"INF" if dist[v] == INF else dist[v]}'
                          for v in sorted(dist))
        lines.append(f'{label:<13} | {values}')
    return lines


def path_line(source, target, dist, prev):
    path = rebuild_path(prev, dist, target)
    if not path:
        return f'{source} to {target}: no path'
    return (f'{source} to {target}: cost {dist[target]}: '
            + ' -> '.join(path))


def main():
    source = 'A'
    dist, prev, states, _ = dijkstra(GRAPH, source)
    for line in format_states(states):
        print(line)
    for target in sorted(GRAPH):
        if target != source:
            print(path_line(source, target, dist, prev))


if __name__ == '__main__':
    main()
