def max_value(r, k, prev_closed, values, cache):
    if r >= len(values):
        return 0 if k == 0 else float('-inf')

    if (r, k, prev_closed) in cache:
        return cache[(r, k, prev_closed)]

    leave_both_open = sum(values[r]) + max_value(r + 1, k, 0, values, cache)

    close_left = float('-inf')
    if k > 0 and not prev_closed == 2:
        close_left = values[r][1] + max_value(r + 1, k - 1, 1, values, cache)

    close_right = float('-inf')
    if k > 0 and not prev_closed == 1:
        close_right = values[r][0] + max_value(r + 1, k - 1, 2, values, cache)

    result = max(leave_both_open, close_left, close_right)

    cache[(r, k, prev_closed)] = result
    return result

def main():
    cache = {}

    while True:
        N, k = map(int, input().split())
        if N == 0 and k == 0:
            break  

        values = [list(map(int, input().split())) for _ in range(N)]

        optimal_value = max_value(0, k, 0, values, cache) 
        print(optimal_value)

if __name__ == "__main__":
    main()
