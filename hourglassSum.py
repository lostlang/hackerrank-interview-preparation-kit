
def hourglass_sum(arr: list) -> int:
    max_sum: int
    sum_indexes: list = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, 0],
        [1, -1],
        [1, 0],
        [1, 1]
    ]
    for i in range(1, 5):
        for j in range(1, 5):
            new_sum = sum([arr[x + i][y + j] for x, y in sum_indexes])
            try:
                max_sum = max(max_sum, new_sum)
            except UnboundLocalError:
                max_sum = new_sum
    return max_sum


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)
    print(result)
