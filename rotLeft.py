
def rot_left(a: list, d: int) -> list:
    out_list = a[d:] + a[:d]
    return out_list


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    a = list(map(int, input().rstrip().split()))

    result = rot_left(a, d)
    print(result)