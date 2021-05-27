
def is_prime(num: int) -> bool:
    i: int = 2
    if num < i:
        return False
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def prime_xor(a: list):
    answer: int = 0
    a_dict = dict()
    mod = pow(10, 9) + 7
    max_i = 8192
    for item in a:
        a_dict[item] = a_dict.get(item, 0) + 1

    dp = [0] * max_i
    dp[0] = 1
    for i in a_dict:
        # i don't understand why it work, but it work
        even, odd = (a_dict[i] // 2 + 1), ((a_dict[i] + 1) // 2)
        dp = [(dp[j] * even + dp[i ^ j] * odd) % mod for j in range(max_i)]

    for i in range(max_i):
        if is_prime(i):
            answer += dp[i]
            if answer > mod:
                answer %= mod
    return answer


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        a = list(map(int, input().rstrip().split()))

        result = prime_xor(a)
        print(result)
