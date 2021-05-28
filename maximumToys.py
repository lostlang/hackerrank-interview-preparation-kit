
def maximum_toys(prices: list, k: int) -> int:
    max_price: int = 0
    count: int = 0
    prices.sort()
    for price in prices:
        if max_price + price < k:
            max_price += price
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))
    result = maximum_toys(prices, k)
    print(result)
