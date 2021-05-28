
def megre_sotr(arr: list) -> int:
    count: int = 0
    if len(arr) > 1:
        left_arr: list = arr[: len(arr) // 2]
        right_arr: list = arr[len(arr) // 2:]
        count += megre_sotr(left_arr)
        count += megre_sotr(right_arr)
        count += merge(arr, left_arr, right_arr)
    return count


def merge(arr: list, arr1: list, arr2: list) -> int:
    count: int = 0
    flag: int
    flag_pre: int
    while arr:
        del arr[0]
    while arr1 and arr2:
        if arr1 and arr2:
            if arr1[0] <= arr2[0]:
                arr.append(arr1[0])
                del arr1[0]
            else:
                arr.append(arr2[0])
                del arr2[0]
                count += len(arr1)
    while arr1:
        arr.append(arr1[0])
        del arr1[0]
    while arr2:
        arr.append(arr2[0])
        del arr2[0]
    return count


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = megre_sotr(arr)
        print(arr)
        print(result)
