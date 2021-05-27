
def minimum_swaps(arr: list) -> int:
    arr: list = [i - 1 for i in arr]

    swaps: int = 0
    temp: list = [0] * (len(arr))
    for pos, val in enumerate(arr):
        temp[val] = pos
    for i in range(len(arr)):
        if arr[i] != i:
            swaps += 1
            tmp = arr[i]
            arr[i] = i
            arr[temp[i]] = tmp
            temp[tmp] = temp[i]
    return swaps


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = minimum_swaps(arr)
    print(res)
