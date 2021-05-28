from functools import cmp_to_key


class Player:
    def __init__(self, name: str, score: int):
        self.name: str = name
        self.score: int = score

    def comparator(a, b):
        if a.score == b.score:
            return -1 if a.name < b.name else 0
        return -1 if a.score > b.score else 0


if __name__ == '__main__':
    n = int(input())
    data = []
    for i in range(n):
        name, score = input().split()
        score = int(score)
        player = Player(name, score)
        data.append(player)

    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)
