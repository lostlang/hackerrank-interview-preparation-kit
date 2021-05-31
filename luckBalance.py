
def luck_balance(k: int, contests: list) -> int:
    luck_score: int = 0
    contests.sort()
    contests.reverse()
    for i in contests:
        if i[1] == 0:
            luck_score += i[0]
        elif k > 0:
            luck_score += i[0]
            k -= 1
        else:
            luck_score -= i[0]
    return luck_score


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luck_balance(k, contests)
    print(result)
