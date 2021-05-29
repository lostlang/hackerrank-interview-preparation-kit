
def alternating_characters(s: str) -> int:
    del_count: int = 0
    start_char: str = s[0]
    for i in range(1, len(s)):
        if s[i] == start_char:
            del_count += 1
        else:
            start_char = s[i]
    return del_count


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()

        result = alternating_characters(s)
        print(result)
