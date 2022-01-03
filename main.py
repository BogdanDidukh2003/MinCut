import sys


class Graph:

    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix
        self.adjacency_matrix_copy = [i[:] for i in adjacency_matrix]
        self.height = len(adjacency_matrix)
        self.width = len(adjacency_matrix[0])

    def bfs(self, source: int, sink: int, parent: list):

        visited = [False] * self.height

        bfs_queue = [source]

        visited[source] = True

        while bfs_queue:

            current_vertex = bfs_queue.pop(0)

            for vertex_position, vertex_value in enumerate(self.adjacency_matrix[current_vertex]):
                if visited[vertex_position] is False and vertex_value > 0:
                    bfs_queue.append(vertex_position)
                    visited[vertex_position] = True
                    parent[vertex_position] = current_vertex

        return True if visited[sink] else False

    def min_cut(self, source: int, sink: int):
        result = []

        parent = [-1] * self.height

        max_flow = 0

        while self.bfs(source, sink, parent):

            path_flow = sys.maxsize
            current_sink = sink
            while current_sink != source:
                path_flow = min(path_flow, self.adjacency_matrix[parent[current_sink]][current_sink])
                current_sink = parent[current_sink]

            max_flow += path_flow

            source_iterator = sink
            while source_iterator != source:
                source_iterator_parent = parent[source_iterator]
                self.adjacency_matrix[source_iterator_parent][source_iterator] -= path_flow
                source_iterator = parent[source_iterator]

        for i in range(self.height):
            for j in range(self.width):
                if self.adjacency_matrix[i][j] == 0 and self.adjacency_matrix_copy[i][j] > 0:
                    result.append([i, j])
                    print(f"{i} -> {j}")
        return result


def main():
    adjacency_matrix = [[0, 16, 13, 0, 0, 0],
                        [0, 0, 10, 12, 0, 0],
                        [0, 4, 0, 0, 14, 0],
                        [0, 0, 9, 0, 0, 20],
                        [0, 0, 0, 7, 0, 4],
                        [0, 0, 0, 0, 0, 0]]

    source = 0
    sink = 5

    count_min_cut(adjacency_matrix, source, sink)


def count_min_cut(adjacency_matrix: list, source: int, sink: int):
    return Graph(adjacency_matrix).min_cut(source, sink)


if __name__ == '__main__':
    main()
