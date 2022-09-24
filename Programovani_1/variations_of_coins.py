def variations(coins, cost, solution=[]):
    if cost == 0:
        print(*solution)
    else:
        for i, money in enumerate(coins):
            if money <= cost:
                variations(coins, cost-money, solution+[money])


if __name__ == "__main__":
    count_of_types = int(input())
    types = list(map(int, input().split()))
    pay = int(input())
    variations(types, pay)
