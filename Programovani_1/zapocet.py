months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def days_to_date(old_full_date, N):
    day, month, year = old_full_date
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        months[1] = 29
    else:
        months[1] = 28
    while day != months[month-1] and N > 0:
        day += 1
        N -= 1
    if N == 0:
        print(day, month, year)
        return
    if day == months[month-1]:
        day = 1
        month += 1
    if month == 13:
        month = 1
        year += 1

    count = 0
    for i in months:
        if count+1 >= month:
            if N > i:
                N -= i
                month += 1
                if month == 13:
                    month = 1
                    year += 1
            else:
                day += N-1
                N = 0
                if month == 13:
                    month = 1
                    year += 1
                break
        count += 1

    if N > 0:
        datee = [day, month, year]
        days_to_date(datee, N-1)
    else:
        print(day, month, year)


date = input().split()
for i in range(len(date)):
    date[i] = int(date[i])

N = int(input())

days_to_date(date, N)
