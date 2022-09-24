def to_decimal(system, number):
    """Using Horner's schema"""
    output_number = 0
    for i in range(len(number)):
        output_number = output_number * system + int(number[i])
    return output_number


def to_x_system(system, number):
    """From decimal system to x system. Back Horner's schema"""
    output_number = ""
    while number > 0:
        output_number = str(number % system) + output_number
        number //= system
    return output_number


if __name__ == "__main__":
    input_data = input().split()
    for j in range(len(input_data)):
        input_data[j] = int(input_data[j])

    final_system = input_data[-1]
    first_number_n_system = input_data[0:2]
    second_number_n_system = input_data[2:4]

    a = to_decimal(system=first_number_n_system[0], number=str(first_number_n_system[1]))
    b = to_decimal(system=second_number_n_system[0], number=str(second_number_n_system[1]))

    answer = [a+b,  a-b,  a*b,  a//b]
    for k in range(len(answer)):
        answer[k] = to_x_system(system=final_system, number=answer[k])

    for element in answer:
        print(element)