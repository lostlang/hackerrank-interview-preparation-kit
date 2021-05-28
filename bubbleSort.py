
def count_swaps(a: list) -> list:
    swaps: int = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    return [swaps, a[0], a[-1]]


def to_out(data: list) -> str:
    template: str = f"Array is sorted in {data[0]} swaps.\n" \
                    f"First Element: {data[1]}\n" \
                    f"Last Element: {data[2]}\n"
    return template


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    ans = count_swaps(a)
    print(to_out(ans))
