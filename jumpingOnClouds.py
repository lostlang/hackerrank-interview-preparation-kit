
def jumping_on_clouds(c: list) -> int:
    jumps: int = 0
    i: int = len(c) - 1
    bad_cloud: int = 1
    while i > 0:
        if c[i - 2] != bad_cloud:
            i -= 2
        else:
            i -= 1
        jumps += 1
    return jumps


if __name__ == '__main__':
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(c)
    print(result)
