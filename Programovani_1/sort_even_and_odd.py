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

    return our_list


if __name__ == "__main__":
    values = input_data()
    answer_list = []

    for val in values:
        if val % 2 == 0:
            answer_list.append(val)
    for val in values:
        if val % 2 == 1:
            answer_list.append(val)

    for i in range(len(answer_list)):
        if i == len(answer_list) - 1:
            print(answer_list[i])
        else:
            print(answer_list[i], end=" ")
