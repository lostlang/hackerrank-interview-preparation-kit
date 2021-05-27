
def minimum_swaps(arr: list) -> int:
    swaps: int
    for i in range(len(arr)):
        if arr[i] != i + 1:
            if arr[arr[i] - 1] != i + 1:
                try:
                    swaps += 1
                except UnboundLocalError:
                    swaps = 0
            elif arr[arr[i] - 1] == i + 1 and arr[i] > i + 1:
                try:
                    swaps += 1
                except UnboundLocalError:
                    swaps = 1
    return swaps


if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = minimum_swaps(arr)
    print(res)
