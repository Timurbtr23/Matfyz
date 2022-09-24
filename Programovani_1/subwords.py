file_name = "vstup.txt" #přídai soubor
data = "" 
answer = {} #udřuje dvojice písmen a jejích počet
with open(file_name, 'r', encoding='utf-8') as file: #základ všech symbolů
    for line in file:
        data += line 
data = data.lower() #děláme malá pisemena

for j in range(len(data)-1): 
    if data[j].isalpha() and data[j+1].isalpha(): #děláme dvojice
        control = data[j:j+2] #máme dvojice
        if control in answer:
            answer[control] += 1 #pokud potkáme dvojice, přidejme
        else:
            answer[control] = 1 ##pokud nepotkáme dvojice, uděláme novou
    else:
        continue

ans_arr = sorted(answer.keys(), key = lambda k: (-answer[k], k)) 
with open("vystup.txt", 'w', encoding='utf-8') as file: #napišeme tabulku v file 
    for key in ans_arr:  
        if key != ans_arr[-1]:
            file.write(" ".join([key, str(answer[key])])+"\n") #курсор на след строку
        else:            
            file.write(" ".join([key, str(answer[key])]))