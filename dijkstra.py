import string


class Vertex(object):
    def __init__(self, obj=None):
        self.obj = obj
        self.neighbours = {}

    def path(self, key, weighting):
        self.neighbours[key] = weighting


def dijkstra(graph, source):
    distances = dict.fromkeys(graph.keys(), float("inf"))
    previous = dict.fromkeys(graph.keys())

    distances[source] = 0
    q = graph.keys()

    while(q):
        u, min_distance = get_shortest_path(q, distances)
        if min_distance == float("inf"):
            break
        q.remove(u)

        # Loop over each neighbour of u
        for key, distance in graph[u].neighbours.iteritems():
            alt = min_distance + distance
            if alt < distances[key]:
                distances[key] = alt
                previous[key] = u
    return distances, previous


def get_shortest_path(q, distances):
    min_distance = float("inf")
    for key in q:
        if distances[key] < min_distance:
            u, min_distance = key, distances[key]
    return u, min_distance


def get_route(previous, source, destination):
    pointer = destination
    route = []
    while(pointer != source):
        pointer = previous[pointer]
        route.append(pointer)
    route.reverse()
    return route


def add_undirected_edge(vertices, a, b, weighting):
    vertices[a].path(b, weighting)
    vertices[b].path(a, weighting)


def create_graph():
    vertices = {}
    for letter in string.lowercase[:6]:
        vertices[letter] = Vertex()

    """
    a - 8 - b - 3 - c
    |     / | \     |
    1   4   1   1   2
    | /     |     \ |
    d - 1 - e - 2 - f
    """

    add_undirected_edge(vertices, "a",  "b",  8)
    add_undirected_edge(vertices, "b",  "c",  3)
    add_undirected_edge(vertices, "a",  "d",  1)
    add_undirected_edge(vertices, "d",  "b",  4)
    add_undirected_edge(vertices, "d",  "e",  1)
    add_undirected_edge(vertices, "e",  "b",  1)
    add_undirected_edge(vertices, "e",  "f",  2)
    add_undirected_edge(vertices, "b",  "f",  1)
    add_undirected_edge(vertices, "c",  "f",  2)

    return vertices


def main():
    vertices = create_graph()
    distances, previous = dijkstra(vertices, "a")
    print "Route"
    print get_route(previous, "a", "c")


if __name__ == "__main__":
    main()
