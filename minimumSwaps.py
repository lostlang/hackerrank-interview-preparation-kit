
def minimum_swaps(arr: list) -> int:
    swaps: int = 0
    swaps_2: int = 0
    swaps_matches: list = []
    for i in range(len(arr)):
        if arr[i] != i + 1:
            if arr[i] not in swaps_matches:
                swaps += 1
                swaps_matches.append(i + 1)
            else:
                if swaps_matches[swaps_matches.index(arr[i])] != i + 1:
                    swaps_2 += 1
                swaps_matches.pop(swaps_matches.index(arr[i]))
    if swaps > 0:
        swaps -= 1
    return swaps + swaps_2


if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = minimum_swaps(arr)
    print(res)
