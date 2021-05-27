
def minimum_swaps(arr: list) -> int:
    swaps: int = -1
    swaps_matches: list = []
    for i in range(len(arr)):
        if i + 1 in swaps_matches:
            if arr[arr[i] - 1] == i + 1:
                pass
            else:
                swaps += 1
        elif arr[i] != i + 1:
            swaps += 1
            swaps_matches.append(arr[i])
    if swaps == -1:
        swaps = 0
    return swaps


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = minimum_swaps(arr)
    print(res)
