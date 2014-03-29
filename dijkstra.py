import string
import copy

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.neighbours = {}

    def to_path(self, name, weighting):
        self.neighbours[name] = weighting

class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices


def main():
    vertices = {}
    for letter in string.lowercase[:6]:
        vertices[letter] = Vertex(letter)

    """
    a - 8 - b - 3 - c
    |     / | \     |
    1   4   1   1   2
    | /     |     \ |
    d - 1 - e - 2 - f
    """

    graph = Graph(vertices)

    add_undirected_edge(vertices["a"], vertices["b"], 8),
    add_undirected_edge(vertices["b"], vertices["c"], 3),
    add_undirected_edge(vertices["a"], vertices["d"], 1),
    add_undirected_edge(vertices["d"], vertices["b"], 4),
    add_undirected_edge(vertices["d"], vertices["e"], 1),
    add_undirected_edge(vertices["e"], vertices["b"], 1),
    add_undirected_edge(vertices["e"], vertices["f"], 2)
    add_undirected_edge(vertices["b"], vertices["f"], 1)
    add_undirected_edge(vertices["c"], vertices["f"], 2)

    distances, previous = dijkstra(graph, "a")
    print "\n\n\n\n", distances
    print "\n\n", previous
    def get_route(previous, source, destination):
        pointer = destination
        route = []
        while(pointer != source):
            pointer = previous[pointer]
            route.append(pointer)
        route.reverse()
        return route

    print "Route"
    print get_route(previous, "a", "c")


def dijkstra(graph, source):
    distances = {}
    for vertex in graph.vertices:
        distances = dict.fromkeys(
            graph.vertices.keys(), float("inf"))
        previous = dict.fromkeys(
            graph.vertices.keys())

    distances[source] = 0
    q = copy.deepcopy(graph.vertices)

    while(q.items()):
        min_distance = float("inf")
        for key, vertex in q.iteritems():
            if distances[key] < min_distance:
                u, min_distance = key, distances[key]
        # if not infinity or none in our case
        if min_distance == float("inf"):
            break

        # remove this key from the queue
        del q[u]

        # Loop over each neighbour of 
        for name, distance in graph.vertices[u].neighbours.iteritems():
            alt = min_distance + distance
            if alt < distances[name]:
                distances[name] = alt
                previous[name] = u
    return distances, previous

def add_undirected_edge(a, b, weighting):
    a.to_path(b.name, weighting)
    b.to_path(a.name, weighting)

if __name__ == "__main__":
    main()
