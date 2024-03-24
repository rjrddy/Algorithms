import heapq


def max_cash(num_people, max_time, person_data):
    person_data.sort(key=lambda x: (x[1], -x[0]))

    total_cash_collected = 0
    cash_heap = []

    for cash_amount, departure_time in person_data:
        if departure_time >= len(cash_heap):
            heapq.heappush(cash_heap, cash_amount)
        elif cash_amount > cash_heap[0]:
            heapq.heappop(cash_heap)
            heapq.heappush(cash_heap, cash_amount)

        while len(cash_heap) > max_time:
            heapq.heappop(cash_heap)

    total_cash_collected = sum(cash_heap)
    return total_cash_collected


if __name__ == "__main__":
    num_people, max_time = map(int, input().split())
    person_data = [tuple(map(int, input().split())) for _ in range(num_people)]
    print(max_cash(num_people, max_time, person_data))
