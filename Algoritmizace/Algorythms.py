def nsd(x, y):
    """Největší společný dělitel
        Eukleidův algoritmus"""

    while y > 0:
        x, y = y, x % y
    print(x)
    return x


def cifsoucet(x):
    """Ciferný součet kladného celého čísla"""

    sum = 0
    while x != 0:
        sum += x % 10
        x //= 10
    print(sum)
    return sum


def prvocislo(n):
    """ Test prvočíselnosti, předpoklad n > 1"""

    if n % 2 == 0:
        return n == 2   # jediné sudé prvočíslo: 2
    d = 3
    while d * d <= n:   # místo volání sqrt(n)
        if n % d == 0:
            return False
        d += 2
    return True


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


def eratosth(n):
    """Eratosthenovo síto"""

    sito = [False, False] + [True] * (n-1)

    i = 2
    while i * i <= n:       # stačí zkoumat čísla do odmocniny z "n"
        if sito[i]:
            j = i * i       # stačí začít s násobky od kvadrátu "i"
            while j <= n:
                sito[j] = False
                j = j + i
        i = i + 1

    prvocisla = []
    for i in range(n+1):
        if sito[i]:
            prvocisla.append(i)

    return prvocisla


def int_to_array(a):
    """Make an array of digits of a number"""

    arr = []
    for j in range(len(str(a))):
        arr.append(int(str(a)[j]))

    return arr


def sum_of_big_numbers(a, b):
    """Chceme počítat například s kladnými celými čísly
        s desítkami nebo stovkami cifer
        DOESN'T WORK!"""

    a = int_to_array(a)
    b = int_to_array(b)

    if len(a) < len(b):
        a, b = b, a     # číslo "a" je delší

    prenos = 0
    c = []
    for i in range(len(b)):
        x = a[i] + b[i] + prenos
        c.append(x % 10)
        prenos = x // 10

    for i in range(len(b), len(a)):
        x = a[i] + prenos
        c.append(x % 10)
        prenos = x // 10

    if prenos > 0:
        c.append(prenos)

    return c


def horner(a, x):
    """
    výpočet hodnoty polynomu Hornerovým schématem
    a: seznam s koeficienty polynomu od nejvyššího řádu
    x: bod z definičního oboru
    vrátí: hodnotu polynomu v bodě x
    """

    h = 0
    for i in range(len(a)):
        h = h * x + a[i]

    return h


a = [2, -5, 0, 4, 6]    # 6x^4 + 4x^3 - 5x + 2
b = [11, 0, -2]        # -2x^2 + 11


def soucet_polynomu(a, b):
    c = []
    if len(a) < len(b):
        a, b = b,a
    for i in range(len(b)):
        c.append(a[i]+b[i])
    for i in range(len(b), len(a)):
        c.append(a[i])
    while len(c) > 1 and c[-1] == 0:
        del c[-1]
    return c


def soucin_polynomu(a, b):
    c = [0] * (len(a)+len(b)-1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] += a[i] * b[j]
    return c


def bin_int(s):
    """
    převod binárního zápisu čísla (string s)
    na číselnou hodnotu.  Hornerovo schéma
    příklad 110010 = ((((1.2 + 1).2 + 0).2 + 0).2 + 1).2 + 0 = 50
    """
    n = 0
    for i in range(len(s)):
        n = n * 2 + int(s[i])
    return n


def hex_int(s):
    """
    převod hexadecimálního zápisu čísla (string s)
    na číselnou hodnotu
    příklad A1F = (10.16 + 1).16 + 15 = 2591
    """

    cifry = "0123456789ABCDEF"
    n = 0
    for i in range(len(s)):
        n = n * 16 + cifry.index(s[i])
    return n


def int_bin(n):
    """ převod čísla do dvojkové soustavy
    - obrácené Hornerovo schéma """

    s = ""
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s


def int_hex(n):
    """ převod čísla do šestnáctkové soustavy
    - obrácené Hornerovo schéma """

    s = ""
    cifry = "0123456789ABCDEF"
    while n > 0:
        s = cifry[n % 16] + s
        n //= 16
    return s


def mocnina2(x, n):
    """výpočet x^n rychleji"""

    v = 1
    while n > 0:
        if n % 2 == 1:
            v *= x
        x *= x
        n //= 2
    return v


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1  # control if -1 print not in the list


def binary_search(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1

#  result = binarySearch(array, x, 0, len(array)-1)

k = 3 # počet prvků v kombinaci
n = 5 # z kolika prvků vybíráme
c = [0] * (k+1) # vytvářená kombinace
# technický trik: c[0]=0, kombinace začíná až v c[1]
def kombinace(p):
 """vypíše všechny k-prvkové kombinace
 z "n" prvků bez opakování,
 "p" je pořadové číslo vybíraného prvku
 (1,2) (1,3) (1,4) (2,3) (2,4) (3,4)
 """
     if p > k:
         print(c[1:])
     else:
         for i in range(c[p-1]+1, n-(k-p)+1):
                c[p] = i
                kombinace(p+1)

    n = 7
    a = [n+1] * (n+1) # prvek a[0] není součástí rozkladu
    def rozklad(z, p):
     """
     z - kolik zbývá rozložit
     p - kolikátý sčítanec vytváříme
     """
     if z == 0: # rozklad je hotov
        print(a[1:p])
     else: # přidáme do a[p] p-tý člen rozkladu
        for i in range(1, min(z, a[p-1])+1):
            a[p] = i
            rozklad(z-i, p+1)
