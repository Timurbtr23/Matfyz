def make_array():
    array = []
    for _ in range(int(input())):
        array.append(input())
    return array


def sort_words_in_array(array):
    new_arr = []
    for word in array:
        new_arr.append("".join(sorted(word)))
    return new_arr


words = sorted(make_array())
controls = make_array()
print(words, controls)

words_s = sort_words_in_array(words)
controls_s = sort_words_in_array(controls)
print(words_s, controls_s)

line = ""
for control_word in controls_s:
    k = 0
    for word in words_s:
        if word == control_word:
            line += words[k] + " "
        k += 1
    print(line[:-1], end="")
    line = ""
    if control_word != controls_s[-1]:
        print()
