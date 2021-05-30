
def common_child(s1: str, s2: str) -> int:
    new_s1: list = [c for c in s1 if c in s2]
    new_s2: list = [c for c in s2 if c in s1]

    lcs_array: list = [[0] * (len(new_s2) + 1) for i in range(len(new_s1) + 1)]

    for i in range(1, len(new_s1) + 1):
        for j in range(1, len(new_s2) + 1):
            if new_s1[i - 1] == new_s2[j - 1]:
                lcs_array[i][j] = lcs_array[i - 1][j - 1] + 1
            else:
                lcs_array[i][j] = max(lcs_array[i][j - 1], lcs_array[i - 1][j])
    return lcs_array[-1][-1]


if __name__ == '__main__':
    s1 = input()
    s2 = input()

    result = common_child(s1, s2)
    print(result)
