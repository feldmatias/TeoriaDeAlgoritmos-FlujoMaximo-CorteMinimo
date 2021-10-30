def bfs(vertices, start):
    # Initialization
    for vertex in vertices:
        vertex.bfs_visited = False
        vertex.bfs_parent = None

    vertices_to_visit = [start]
    start.bfs_visited = True
    index = 0

    # BFS algorithm
    while index < len(vertices_to_visit):
        vertex = vertices_to_visit[index]

        # Analyze neighbours
        for edge in vertex.edges:
            neighbour = edge.vertex_to
            if neighbour.bfs_visited or edge.weight == 0:
                continue
            neighbour.bfs_visited = True
            neighbour.bfs_parent = edge
            vertices_to_visit.append(neighbour)

        index += 1

    return vertices


