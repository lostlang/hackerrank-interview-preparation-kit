from bisect import bisect_left, insort_left


def activity_notifications(expenditure: list, d: int) -> int:
    frauds: int = 0
    fraud: int
    test: list = expenditure[:d]
    test.sort()
    for i in range(d, len(expenditure)):
        fraud = test[len(test) // 2] if len(test) % 2 else sum(test[len(test) // 2 - 1: len(test) // 2 + 1]) / 2
        fraud *= 2
        if expenditure[i] >= fraud:
            frauds += 1
        del test[bisect_left(test, expenditure[i - d])]
        insort_left(test, expenditure[i])
    return frauds


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    expenditure = list(map(int, input().rstrip().split()))

    result = activity_notifications(expenditure, d)
    print(result)
