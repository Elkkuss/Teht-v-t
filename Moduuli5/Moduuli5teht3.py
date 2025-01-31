def main():
    print("Anna luku")
    user_input = int(input("> "))

    if prime_num_check(user_input):
        print("Numero on alkuluku")
    else:
        print("Numero ei ole alkuluku")


def prime_num_check(num):
    for i in range(2, num - 1):
        if num % i == 0:
            return False
        else:
            pass
    return True


main()