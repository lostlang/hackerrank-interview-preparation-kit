
def array_manipulation(n: int, queries: list) -> int:
    max_manipulation: int = 0
    q: dict = dict()
    for i in queries:
        try:
            q[i[0]] += i[2]
        except KeyError:
            q[i[0]] = i[2]

        try:
            q[i[1] + 1] -= i[2]
        except KeyError:
            q[i[1] + 1] = -i[2]

    keys: list = list(q.keys())
    keys.sort()
    manipulation: int = 0
    for key in keys:
        manipulation += q[key]
        max_manipulation = max(max_manipulation, manipulation)
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
