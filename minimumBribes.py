
def minimum_bribes(q: list):
    max_swap: int = 2

    new_q: list = []
    max_q: list = [q[0]]

    for i in range(len(q) - 1):
        if q[i + 1] - q[i] == 1:
            max_q.append(q[i + 1])
        else:
            new_q.append(max_q)
            max_q = [q[i + 1]]
    else:
        new_q.append(max_q)

    swaps: list = [0 for i in new_q]

    while True:
        tmp_swap = 1
        for i in range(len(new_q) - 1):
            if new_q[i][-1] > new_q[i + 1][0]:
                tmp_swap = 0
                swaps[i] += len(new_q[i + 1]) * len(new_q[i])
                swaps[i], swaps[i + 1] = swaps[i + 1], swaps[i]
                new_q[i], new_q[i + 1] = new_q[i + 1], new_q[i]
        if tmp_swap:
            break

    for i in range(len(new_q)):
        if swaps[i] <= len(new_q[i]) * max_swap:
            continue
        else:
            return "Too chaotic"

    return sum(swaps)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))

        result = minimum_bribes(q)
        print(result)
