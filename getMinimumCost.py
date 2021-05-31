
def get_minimum_cost(k: int, c: list) -> int:
    cost: int = 1
    cost_all: int = 0
    c.sort()
    c.reverse()
    print(c)
    for i in range(len(c)):
        cost_all += cost * c[i]
        if not (i + 1) % k:
            cost += 1
    return cost_all


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))

    result = get_minimum_cost(k, c)
    print(result)
