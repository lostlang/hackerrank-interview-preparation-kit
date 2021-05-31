
def minimum_absolute_difference(arr: list) -> int:
    arr.sort()
    min_abs: int
    for i in range(len(arr) - 1):
        try:
            min_abs = min(min_abs, abs(arr[i] - arr[i + 1]))
        except UnboundLocalError:
            min_abs = abs(arr[i] - arr[i + 1])
    return min_abs


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = minimum_absolute_difference(arr)
    print(result)
