from bfs import bfs


def max_flow_min_cut(vertices, start, end):
    """ Calculate max flow in graph using Ford-Fulkerson + Edmonds-Karp algorithm"""

    max_flow = 0  # There is no flow initially

    while True:
        bfs(vertices, start)

        if not end.bfs_visited:
            # There is no path between start and end
            break

        path = end.get_bfs_path()
        bottleneck = min([edge.weight for edge in path])

        # Update edges and residual edges values
        for edge in path:
            edge.weight -= bottleneck
            edge.inverse_edge.weight += bottleneck
        max_flow += bottleneck

    min_cut = calculate_min_cut(vertices, start)
    return max_flow, min_cut


def calculate_min_cut(vertices, start):
    # Calculate vertices that are reachable from start in residual graph
    bfs(vertices, start)
    reachable_vertices = set()
    unreachable_vertices = set()

    for vertex in vertices:
        if vertex.bfs_visited:
            reachable_vertices.add(vertex)
        else:
            unreachable_vertices.add(vertex)

    # Edges belong to min cut if:
    #  1- they go from a reachable vertex to an unreachable vertex
    #  2- they are original edges (not residual)
    #  3- they have weight 0 after Ford-Fulkerson (this will always happen because of 1)

    min_cut = []
    for vertex in reachable_vertices:
        for edge in vertex.edges:
            if not edge.residual and edge.weight == 0 and edge.vertex_to in unreachable_vertices:
                min_cut.append(edge)
    return min_cut
