class Vertex:
    def __init__(self, name, id):
        self.name = name
        self.id = id + 1

        self.edges = []

        self.bfs_visited = False
        self.bfs_parent = None

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __hash__(self):
        return hash(self.name)

    def get_bfs_path(self):
        path = []
        edge = self.bfs_parent
        while edge:
            path.append(edge)
            edge = edge.vertex_from.bfs_parent
        return list(reversed(path))

