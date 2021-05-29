
def get_counter(items: str or list) -> dict:
    out_dict: dict = dict()
    for i in items:
        out_dict[i] = out_dict.get(i, 0) + 1
    return out_dict


def is_valid(s: str) -> str:
    str_count: dict = get_counter(s)
    value_count: dict = get_counter(str_count.values())
    if len(value_count) > 2:
        return "NO"
    elif len(value_count) in [0, 1]:
        return "YES"
    value_count_items: list = [(i, value_count[i]) for i in sorted(value_count)]
    if value_count_items[0][0] + 1 == value_count_items[1][0] and value_count_items[1][1] == 1 or\
            value_count_items[0][0] == 1 and value_count_items[0][1] == 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    s = input()

    result = is_valid(s)
    print(result)
