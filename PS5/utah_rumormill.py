class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex1].sort()
            self.adjacency_list[vertex2].append(vertex1)
            self.adjacency_list[vertex2].sort()

    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])

    def bfs(self, initial_vertex):
        if initial_vertex not in self.adjacency_list:
            return [initial_vertex] + sorted([student for student in self.adjacency_list if student != initial_vertex])

        visited = {initial_vertex}
        queue = [initial_vertex]
        order = [initial_vertex]

        while queue:
            current_level = []
            while queue:
                vertex = queue.pop(0)
                for neighbor in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        current_level.append(neighbor)
            order.extend(sorted(current_level))
            queue.extend(current_level)

        unheard_students = [student for student in sorted(self.adjacency_list) if student not in visited]
        order.extend(unheard_students)
        return order


def main():
    n = int(input())
    students = Graph()

    for i in range(n):
        student = input()
        students.add_vertex(student)

    f = int(input())

    for i in range(f):
        friend1, friend2 = input().split()
        students.add_edge(friend1, friend2)

    r = int(input())

    for i in range(r):
        student = input()
        result = students.bfs(student)
        for j in range(len(result)):
            print(result[j], end=' ')
        print()


if __name__ == "__main__":
    main()
