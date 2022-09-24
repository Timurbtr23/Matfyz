if __name__ == "__main__":

    input_data = []
    with open("a.txt", mode='r', encoding='utf8') as file:
        for line in file:
            input_data.append(line)

    # Split by ". " and remove all \n
    input_data = " ".join(input_data).split(". ")
    data = []
    for x in input_data:
        data.append(x.replace("\n", ""))

    # Make "." at the end of every sentence
    for k in range(len(data)):
        if data[k][-1] != '.':
            data[k] += '.'

    # Write down all sentences
    with open("b.txt", mode='w', encoding='utf8') as file:
        for j in range(len(data)):
            if data[j] != data[-1]:
                file.write(data[j] + "\n")
            else:
                file.write(data[j])
