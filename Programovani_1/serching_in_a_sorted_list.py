def input_values(stop):
    our_list = []

    count = 0
    while count < stop:
        line = input().split()

        for number in line:
            our_list.append(int(number))

        count = len(our_list)

    if count > stop:
        our_list = our_list[0:stop]

    return our_list


def binary_search(array, x, answer):
    def search_to_left(position, array):
        new_position = position
        while True:
            if array[position-1] == array[position]:
                position -= 1
                new_position = position
                continue
            else:
                return new_position
    start = 0
    end = len(array) - 1
    center = (start + end) // 2
    while array[center] != x and start <= end:
        if x > array[center]:
            start = center + 1
        else:
            end = center - 1
        center = (start + end) // 2
    if x == array[center]:
        answer.append(search_to_left(position=center, array=array) + 1)
    else:
        answer.append(0)


if __name__ == "__main__":
    input_data = input().split()
    for i in range(len(input_data)):
        input_data[i] = int(input_data[i])

    values = input_values(input_data[0])
    check_data = input_values(input_data[1])
    answer_list = []

    for element in check_data:
        binary_search(values, element, answer_list)

    for i in range(len(answer_list)):
        if i == len(answer_list) - 1:
            print(answer_list[i])
        else:
            print(answer_list[i], end=" ")
