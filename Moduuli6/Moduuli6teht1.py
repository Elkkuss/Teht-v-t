def main():
    while True:
        luku = noppa()
        print(luku)
        if luku == 6:
            break
        else:
            pass

def noppa():
    from random import randint
    return randint(1,6)

main()
