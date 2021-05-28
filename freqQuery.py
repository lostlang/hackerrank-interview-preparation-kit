
def freq_query(queries: list) -> list:
    queries_dict: dict = dict()
    selectors: list = [1, 2, 3]
    answers: list = []
    for q in queries:
        if q[0] == selectors[0]:
            queries_dict[q[1]] = queries_dict.get(q[1], 0) + 1
        elif q[0] == selectors[1]:
            try:
                queries_dict[q[1]] = max(0, queries_dict[q[1]] - 1)
            except KeyError:
                pass
        elif q[0] == selectors[2]:
            answers.append(q[1] in set(queries_dict.values()))
        else:
            raise Exception("Not valid selector")
    return answers


def to_out(arr: list) -> str:
    to_int = lambda x: "1" if x else "0"
    return "\n".join(list(map(to_int, arr)))


if __name__ == '__main__':
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freq_query(queries)
    print(to_out(ans))
