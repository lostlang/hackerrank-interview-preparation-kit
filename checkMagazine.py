
def check_magazine(magazine: list, note: list) -> str:
    worlds: dict = {}
    for word in magazine:
        worlds[word] = worlds.get(word, 0) + 1
    for word in note:
        if worlds.get(word, 0) == 0:
            return "No"
        else:
            worlds[word] -= 1
    return "Yes"


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()

    res = check_magazine(magazine, note)
    print(res)
