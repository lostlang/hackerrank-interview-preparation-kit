
def get_counter(items: str or list) -> dict:
    out_dict: dict = dict()
    for i in items:
        out_dict[i] = out_dict.get(i, 0) + 1
    return out_dict


def substring_count(s: str):
    count: int = 0
    for i in range(1, len(s)):
        for j in range(i + 1, len(s) + 1):
            if len(set(s[i:j])) == 1 and s[i:j] == s[j - 1:i - 1:-1]:
                print(s[i:j])
                count += 1
            elif len(set(s[i:j])) > 2:
                break
            elif len(set(s[i:j])) == 2 and min(get_counter(s[i:j]).values()) > 1:
                break
            elif s[i:j] == s[j - 1:i - 1:-1]:
                print(s[i:j])
                count += 1
    for j in range(1, len(s) + 1):
        if len(set(s[:j])) == 1 and s[:j] == s[j - 1::-1]:
            print(s[:j])
            count += 1
        elif len(set(s[:j])) > 2:
            break
        elif len(set(s[:j])) == 2 and min(get_counter(s[:j]).values()) > 1:
            break
        elif s[:j] == s[j - 1::-1]:
            print(s[:j])
            count += 1
    return count


if __name__ == '__main__':
    n = int(input())
    s = input()

    result = substring_count(s)
    print(result)
