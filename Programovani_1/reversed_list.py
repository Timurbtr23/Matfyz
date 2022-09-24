def input_data():
    our_list = []

    break_it = False
    while not break_it:
        line = input().split()

        for number in line:
            if number == "-1":
                break_it = True
                break
            our_list.append(int(number))

    return list(reversed(our_list))


if __name__ == "__main__":
    values = input_data()

    for i in range(len(values)):
        if i == len(values) - 1:
            print(values[i])
        else:
            print(values[i], end=" ")
