#!/usr/bin/env python3

import sys


def prime_power(n):
    """
    Function return prime power of n
    :param n: input number, type int,n > 1
    :return: list of prime power numbers
    """
    prvocisla = []

    while n % 2 == 0:
        prvocisla.append(2)
        n //= 2
        if n == 1:
            return prvocisla

    i = 3
    while i <= n:
        while n % i == 0:
            prvocisla.append(i)
            n //= i
        if n == 1:
            return prvocisla
        i += 2

    return prvocisla


def main():

    number = sys.argv[1]

    if not number.isnumeric():
        print('-')
        return
    else:
        number = int(number)

    if number <= 0:
        print('-')
        return

    prime_numbers = prime_power(number)
    for i in prime_numbers:
        print(i)


if __name__ == '__main__':
    main()
