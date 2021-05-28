
def megre_sotr(arr: list, start_arr: int, end_arr: int) -> int:
    count: int = 0
    if start_arr >= end_arr:
        return count
    middle: int = start_arr + (end_arr - start_arr) // 2
    count += megre_sotr(arr, start_arr, middle)
    count += megre_sotr(arr, middle + 1, end_arr)
    count += merge(arr, start_arr, middle, end_arr)
    return count


def merge(arr: list, start_arr: int, middle_arr: int, end_arr: int) -> int:
    count: int = 0
    new_arr: list = []
    i: int = start_arr
    j: int = middle_arr + 1
    while i <= middle_arr and j <= end_arr:
        if arr[i] <= arr[j]:
            new_arr.append(arr[i])
            i += 1
        else:
            new_arr.append(arr[j])
            j += 1
            count += middle_arr - i + 1
    while i <= middle_arr:
        new_arr.append(arr[i])
        i += 1
    while j <= end_arr:
        new_arr.append(arr[j])
        j += 1
    arr[start_arr:end_arr + 1] = new_arr
    return count


def count_inversions(arr: list):
    return megre_sotr(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = count_inversions(arr)
        print(arr)
        print(result)
