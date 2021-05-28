
def get_counter(s: list) -> dict:
    s_dict: dict = dict()
    for i in s:
        s_dict[i] = s_dict.get(i, 0) + 1
    return s_dict


def count_triplets(arr: list, r: int):
    triplets: int = 0
    arr_counter: dict = get_counter(arr)
    arr_counter2: dict = dict()
    for i in arr:
        pre = i // r
        past = i * r
        arr_counter[i] -= 1
        if arr_counter2.get(pre, 0) and arr_counter.get(past, 0) and not i % r:
            triplets += arr_counter2.get(pre, 0) * arr_counter.get(past, 0)
        arr_counter2[i] = arr_counter2.get(i, 0) + 1
    return triplets


if __name__ == '__main__':
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))

    ans = count_triplets(arr, r)
    print(ans)
