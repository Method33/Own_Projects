import heapq

def dijkstra(graph, start_node):
    """
    Implementing Dijkstra's Algorithm to find the shortest path in a graph.
    """

    shortest_paths = {start_node: (None, 0)}
    queue = [(0, start_node)]
    while queue:
        (dist, current_node) = heapq.heappop(queue)

        for neighbor, distance in graph[current_node].items():
            old_distance = shortest_paths.get(neighbor, (None, float('inf')))[1]
            new_distance = dist + distance

            if new_distance < old_distance:
                shortest_paths[neighbor] = (current_node, new_distance)
                heapq.heappush(queue, (new_distance, neighbor))

    result = {}
    for node, (previous_node, shortest_distance) in shortest_paths.items():
        path = []
        while previous_node is not None:
            path.append(node)
            node = previous_node
        if path:
            path.append(start_node)
        result[node] = path[::-1]

    return result
