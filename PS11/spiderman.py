def spiderman_workout(distances):
    n = len(distances)
    max_height = sum(distances)
    dp = [[None] * (max_height + 1) for _ in range(n + 1)]
    dp[0][0] = (True, "")

    for i in range(1, n + 1):
        for j in range(max_height + 1):
            if j - distances[i - 1] >= 0 and dp[i - 1][j - distances[i - 1]] and dp[i - 1][j - distances[i - 1]][0]:
                dp[i][j] = (True, dp[i - 1][j - distances[i - 1]][1] + "U")
            elif j + distances[i - 1] <= max_height and dp[i - 1][j + distances[i - 1]] and dp[i - 1][j + distances[i - 1]][0]:
                dp[i][j] = (True, dp[i - 1][j + distances[i - 1]][1] + "D")

    for final_height in range(max_height + 1):
        if dp[n][final_height] and dp[n][final_height][0]:
            return dp[n][final_height][1]

    return "IMPOSSIBLE"


def main():
    num_cases = int(input())
    for _ in range(num_cases):
        num_distances = int(input())
        distances = list(map(int, input().split()))
        print(spiderman_workout(distances))

if __name__ == "__main__":
    main()
