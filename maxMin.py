
def max_min(k: int, arr: list) -> int:
    arr.sort()
    return min(arr[i + k - 1] - arr[i] for i in range(len(arr) - k + 1))


if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = max_min(k, arr)
    print(result)
