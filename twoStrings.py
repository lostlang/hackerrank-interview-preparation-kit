
def two_strings(s1: str, s2: str) -> str:
    s1_set: set = set(s1)
    s2_set: set = set(s2)
    if s1_set & s2_set:
        return "YES"
    return "NO"


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s1 = input()
        s2 = input()

        result = two_strings(s1, s2)
        print(result)
