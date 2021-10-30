from Edge import Edge
from Vertex import Vertex


def parse_file(filename):
    data = []
    start = None
    end = None
    with open(filename) as f:
        for index, line in enumerate(f.readlines()):
            if index == 0:
                start = line.strip('\n')
            elif index == 1:
                end = line.strip('\n')
            else:
                origin, destination, weight = line.split(',')
                data.append((origin, destination, int(weight)))
    return data, start, end


def create_graph(filename):
    data, start, end = parse_file(filename)
    vertices = {}

    for line in data:
        from_name, to_name, weight = line

        vertex_from = vertices.get(from_name, Vertex(from_name, id=len(vertices)))
        vertices[from_name] = vertex_from

        vertex_to = vertices.get(to_name, Vertex(to_name, id=len(vertices)))
        vertices[to_name] = vertex_to

        # Create edge and residual edge
        edge = Edge(vertex_from, vertex_to, weight, residual=False)
        residual_edge = Edge(vertex_to, vertex_from, 0, residual=True)

        edge.inverse_edge = residual_edge
        residual_edge.inverse_edge = edge

        vertex_from.edges.append(edge)
        vertex_to.edges.append(residual_edge)

    return list(vertices.values()), vertices.get(start), vertices.get(end)
