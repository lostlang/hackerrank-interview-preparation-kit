
def make_anagram(a: str, b: str):
    del_count: int = 0
    sorted_a: list = sorted(a)
    sorted_b: list = sorted(b)
    while sorted_a and sorted_b:
        if sorted_a[0] == sorted_b[0]:
            del sorted_a[0]
            del sorted_b[0]
        elif sorted_a[0] > sorted_b[0]:
            del sorted_b[0]
            del_count += 1
        else:
            del sorted_a[0]
            del_count += 1
    del_count += len(sorted_a) + len(sorted_b)
    return del_count


if __name__ == '__main__':
    a = input()
    b = input()

    res = make_anagram(a, b)
    print(res)
