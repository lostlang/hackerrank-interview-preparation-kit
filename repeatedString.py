
def repeated_string(s: str, n: int):
    need_letter: str = "a"
    a_in_s = n // len(s) * s.count(need_letter)
    if n > len(s):
        a_in_s += s[:n % len(s)].count(need_letter)
    elif n < len(s):
        a_in_s += s[:n].count(need_letter)
    return a_in_s


if __name__ == '__main__':
    s = input()
    n = int(input().strip())

    result = repeated_string(s, n)
    print(result)
