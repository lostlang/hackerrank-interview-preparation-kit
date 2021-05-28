
def get_counter(s: str) -> dict:
    s_dict: dict = dict()
    for i in s:
        s_dict[i] = s_dict.get(i, 0) + 1
    return s_dict


def matches(n: int) -> int:
    return sum(range(n + 1))


def sherlock_and_anagrams(s: str) -> int:
    anagrams: int
    s_dict: dict
    all_dict: list = []
    all_dict_count: list = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            s_dict = get_counter(s[i:j])
            if s_dict not in all_dict:
                all_dict.append(s_dict)
                all_dict_count.append(0)
            else:
                all_dict_count[all_dict.index(s_dict)] += 1
    anagrams = sum(map(matches, all_dict_count))
    return anagrams


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()

        result = sherlock_and_anagrams(s)
        print(result)
