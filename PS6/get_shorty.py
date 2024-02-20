import heapq

class Graph:
    def __init__(self, num_intersections):
        self.num_intersections = num_intersections
        self.edges = [[] for _ in range(num_intersections)]
        
    def add_corridor(self, u, v, factor):
        self.edges[u].append((v, factor))
        self.edges[v].append((u, factor))
    
    def shortest_path(self):
        distances = [0] * self.num_intersections
        distances[0] = 1
        pq = [(-1, 0)]

        while pq:
            current_factor, current_vertex = heapq.heappop(pq)
            current_factor = -current_factor

            if current_factor < distances[current_vertex]:
                continue

            for neighbor, factor in self.edges[current_vertex]:
                new_factor = current_factor * factor

                if new_factor > distances[neighbor]:
                    distances[neighbor] = new_factor
                    heapq.heappush(pq, (-new_factor, neighbor))
                    
        return f"{distances[-1]:.4f}"

    
def main():
    while True: 
        n,m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        corridor_map = Graph(n)
        
        for i in range(m):
            x,y,factor = input().split()
            x, y = int(x), int(y)
            factor = float(factor)
            corridor_map.add_corridor(x, y, factor)
        
        fastest_path = corridor_map.shortest_path()
        print(fastest_path)
        
        continue
    
if __name__ == "__main__":
    main()
