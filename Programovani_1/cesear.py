def decrypting(data, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for letter in data:
        if letter in alphabet:
            for j in range(len(alphabet)):
                if letter == alphabet[j]:
                    answer += alphabet[(j + (k % 26)) % 26]
                    break
        else:
            answer += letter
    return answer.upper()


if __name__ == "__main__":
    k = int(input())
    data = input()
    print(decrypting(data.lower(), k))
