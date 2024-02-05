
# utah_galaxyquest.py by Raj Reddy for CS 4150 (1/24/24) coded in Python

def star_distance(x1, x2, y1, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def find_majority(stars, d):
    if len(stars) == 0:
        return 0, None
    if len(stars) == 1:
        return 1, stars[0]

    mid = len(stars) // 2
    x_arr = stars[:mid]
    y_arr = stars[mid:]

    x_num, x = find_majority(x_arr, d)
    y_num, y = find_majority(y_arr, d)

    if x_num == 0 and y_num == 0:
        return 0, None
    elif x_num == 0:
        y_num = count_stars(y, stars, d)
        if y_num > mid:
            return y_num, y
        else:
            return 0, None
    elif y_num == 0:
        x_num = count_stars(x, stars, d)
        if x_num > mid:
            return x_num, x
        else:
            return 0, None
    else:
        y_num = count_stars(y, stars, d)
        x_num = count_stars(x, stars, d)

        if x_num > mid:
            return x_num, x
        elif y_num > mid:
            return y_num, y
        else:
            return 0, None


def count_stars(core_star, stars, d):
    d_squared = d ** 2
    count = 0
    for star in stars:
        if star_distance(core_star[0], star[0], core_star[1], star[1]) <= d_squared:
            count += 1
    return count


def main():
    d, k = map(int, input().split())
    all_vals = []

    for i in range(k):
        vals = list(map(int, input().split()))
        all_vals.append(vals)

    result = find_majority(all_vals, d)

    return result


if __name__ == "__main__":
    result, core_star = main()
    if result:
        print(result)
    else:
        print("NO")
