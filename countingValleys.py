
def counting_valleys(steps: int, path: str) -> int:
    valleys: int = 0
    height: int = 0
    state_path_down: str = "D"
    for i in path:
        if i == state_path_down:
            height -= 1
        else:
            height += 1
            if height == 0:
                valleys += 1
    return valleys


if __name__ == '__main__':
    steps = int(input().strip())
    path = input()

    result = counting_valleys(steps, path)
    print(result)
