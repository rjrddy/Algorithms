class Graph:
    def __init__(self, num_vertices):
        self.graph = {}
        self.V = num_vertices

    def add_edge(self, u, v, toll):
        if u in self.graph:
            self.graph[u].append((v, toll))
        else:
            self.graph[u] = [(v, toll)]

    def top_sort(self, v, visited, stack):
        visited[v] = True
        for i, _ in self.graph.get(v, []):
            if not visited[i]:
                self.top_sort(i, visited, stack)
        stack.insert(0, v) 

    def shortestPath(self, tolls):
        min_tolls = [[float('Inf') for _ in range(self.V)]
                     for _ in range(self.V)]
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.top_sort(i, visited, stack)

        for s in range(self.V):
            dist = [float('Inf')] * self.V
            dist[s] = 0

            for i in stack:
                if dist[i] != float('Inf'):
                    for node, weight in self.graph.get(i, []):
                        if dist[node] > dist[i] + weight:
                            dist[node] = dist[i] + weight

            for i in range(self.V):
                min_tolls[s][i] = dist[i]

        for i in range(self.V):
            for j in range(self.V):
                if min_tolls[i][j] == float('Inf'):
                    min_tolls[i][j] = "NO"

        return min_tolls


def main():

    n = int(input())
    tolls = {}
    cities = {}
    city_index = {}

    for i in range(n):
        city, toll = input().split()
        toll = int(toll)
        cities[i] = city
        tolls[i] = toll
        city_index[city] = i

    h = int(input())
    highway = Graph(n)

    for _ in range(h):
        u_city, v_city = input().split()
        u = city_index.get(u_city)
        v = city_index.get(v_city)
        if u is None or v is None:
            print("City name error.")
            return
        highway.add_edge(u, v, tolls[v])

    shortest_tolls = highway.shortestPath(tolls)

    t = int(input())
    for _ in range(t):
        from_city, to_city = input().split()
        from_index = city_index.get(from_city)
        to_index = city_index.get(to_city)
        if from_index is None or to_index is None or from_index >= n or to_index >= n:
            print("NO") 
        else:
            print(shortest_tolls[from_index][to_index])


if __name__ == "__main__":
    main()
