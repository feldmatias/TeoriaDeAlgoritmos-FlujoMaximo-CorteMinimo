class Edge:

    def __init__(self, vertex_from, vertex_to, weight, residual=False):
        self.vertex_from = vertex_from
        self.vertex_to = vertex_to
        self.weight = weight
        self.original_weight = weight
        self.residual = residual
        self.inverse_edge = None

    def __str__(self):
        return f"{self.vertex_from} -> {self.vertex_to}"
