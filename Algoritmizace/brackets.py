if __name__ == "__main__":
    # TODO Pro zásobník použijte seznam a jeho metody [].append() a [].pop() Nerozumim kde a proc to mam pouzit
    open_brackets = ["(", "<", "{", "["]
    close_brackets = [")", ">", "}", "]"]
    data_brackets = []
    data = input()

    count = 0
    for i in data:
        if count < 0:
            break
        if i in open_brackets:
            count += 1

        elif i in close_brackets:
            count -= 1

    if count == 0:
        print("True")
    elif count == -1:
        print("False")
