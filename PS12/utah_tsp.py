import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    
    adj_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(data[idx]))
            idx += 1
        adj_matrix.append(row)

    FULL_MASK = (1 << n) - 1
    dp = [[float('inf')] * (FULL_MASK) for _ in range(n)]
    next_node = [[-1] * (FULL_MASK) for _ in range(n)]

    for i in range(n):
        dp[i][0] = adj_matrix[i][0]

    for mask in range(FULL_MASK):
        for u in range(n):
            if mask & (1 << u):
                continue
            for v in range(n):
                if not mask & (1 << v):
                    continue
                new_mask = mask ^ (1 << v)
                if dp[u][mask] > dp[v][new_mask] + adj_matrix[u][v]:
                    dp[u][mask] = dp[v][new_mask] + adj_matrix[u][v]
                    next_node[u][mask] = v

    min_cost = dp[0][FULL_MASK - 1]
    print(min_cost)

if __name__ == "__main__":
    main()