
def array_manipulation(n: int, queries: list) -> int:
    max_manipulation: int
    q: list = [0] * n
    for i in queries:
        for j in range(i[0] - 1, i[1]):
            q[j] += i[2]
    max_manipulation = max(q)
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
