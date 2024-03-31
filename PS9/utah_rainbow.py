
def min_cost(distances):
    n = len(distances) - 1
    min_pen = [float('inf')] * (n + 1)
    min_pen[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            curr = (distances[i] - distances[j] - 400) ** 2
            min_pen[i] = min(min_pen[i], min_pen[j] + curr)

    return min_pen[n]


def main():
    n = int(input())
    distances = []
    for i in range(n+1):
        distance = int(input())
        distances.append(distance)

    lowest_cost = min_cost(distances)
    print(lowest_cost)


if __name__ == "__main__":
    main()
