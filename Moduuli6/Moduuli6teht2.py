def main():
    print("Anna nopan maksimisilmäluku. ")
    user_input = int(input("> " ))
    while True:

        result = dice(user_input)
        print(result)
        if result == user_input:
            break
        else:
            pass

def dice(max):
    from random import randint
    return randint(1,max)

    





main()