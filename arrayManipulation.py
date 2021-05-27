
def array_manipulation(n: int, queries: list) -> int:
    max_manipulation: int
    q: list = [[1, n, 0]]
    for i in queries:
        j = 0
        while j < len(q):
            if q[j][0] < i[0] <= q[j][1]:
                q.insert(j + 1, [i[0], q[j][1], q[j][2]])
                q[j][1] = i[0] - 1
            if q[j][0] < i[1] < q[j][1]:
                q.insert(j, [q[j][0], i[1], q[j][2]])
                q[j + 1][0] = i[1] + 1
            j += 1

        for j in q:
            if j[0] >= i[0] and j[1] <= i[1]:
                j[2] += i[2]
        j = 0
        while j < len(q) - 1:
            if q[j][2] == q[j + 1][2]:
                q[j][1] = q[j + 1][1]
                del q[j + 1]
            else:
                j += 1
    max_manipulation = max([i[2] for i in q])
    return max_manipulation


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = array_manipulation(n, queries)
    print(result)
