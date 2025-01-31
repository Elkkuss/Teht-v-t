def main():
    print("Anna kokonaislukuja listaan")
    lista = []
    while True:
        user_input = input("> ")
        if user_input == "":
            break
        else:
            lista.append(int(user_input))
    print(lista)
    print(parittomat_luvut(lista))


def parittomat_luvut(lista):
    for i in lista:
        if i % 2 == 0:
            pass
        else:
            lista.remove(i)
    return lista

main()