
def sock_merchant(n: int, ar: list) -> int:
    d: dict = dict()
    for i in ar:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1

    matches: int = 0
    for i in d:
        matches += d[i] // 2
    return matches


if __name__ == '__main__':

    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(n, ar)
    print(result)
