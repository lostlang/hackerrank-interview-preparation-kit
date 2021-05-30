
def common_child(s1: str, s2: str) -> int:
    count: int = 0
    set_s1: set = set(s1)
    set_s2: set = set(s2)
    new_s1: str = ""
    new_s2: str = ""
    xor_set: set = set_s1 ^ set_s2

    for i in s1:
        if i not in xor_set:
            new_s1 = new_s1 + i

    for i in s2:
        if i not in xor_set:
            new_s2 = new_s2 + i

    lcs_array: list = [[0] * (len(new_s2) + 1) for i in range(len(new_s1) + 1)]

    for i in range(1, len(new_s1) + 1):
        for j in range(1, len(new_s2) + 1):
            if new_s1[i - 1] == new_s2[j - 1]:
                lcs_array[i][j] = lcs_array[i - 1][j - 1] + 1
            else:
                lcs_array[i][j] = max(lcs_array[i][j - 1], lcs_array[i - 1][j])
            count = max(count, lcs_array[i][j])
    return count


if __name__ == '__main__':
    s1 = input()
    s2 = input()

    result = common_child(s1, s2)
    print(result)
