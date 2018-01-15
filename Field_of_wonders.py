word= "книга"
pole="*"*len(word)
print(pole)
while '*' in pole:
    user= input("Угадай букуву в этом словеили слово целиком: ")
    dop = ""
    for nomer in range(len(word)):
        if user==word[nomer]:
            dop += user
        else:
            dop += pole[nomer]
    pole=dop
    print(pole)
print("Молодец! Угадал слово", word)