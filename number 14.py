import random
UPPER_DIGIT = 100
LOWER_DIGIT = 1

def main():
    print("""
    Вам необходимо угадать число от 1 до 100
    по ходу отгадывания вам будут посылаться подсказки
    """)
    fl = want_to_continue()
    while fl:
        our_digit = generation_of_digits()
        print(our_digit)
        your_digit = int(input("введите число от 1 до 100\t"))
        while check_input_one(your_digit):
            your_digit = int(input("число должно быть в пределах от 1 до 100"))
        k = 1
        while (your_digit != our_digit):
            k += 1
            more_or_less(our_digit, your_digit)
            your_digit = int(input("введите число от 1 до 100\t"))
            while check_input_one(your_digit):
                your_digit = int(input("число должно быть в пределах от 1 до 100"))
        print("поздравляю, вы угадали число с", k, "раза")
        fl = want_to_continue()


def generation_of_digits():
    return random.randint(LOWER_DIGIT, UPPER_DIGIT)

def check_input_one(your_digit):
    return (your_digit < 1) or (your_digit > 100)

def yes_or_no(our_digit, your_digit):
    return our_digit == your_digit

def more_or_less(our_digit, your_digit):
    if (our_digit > your_digit):
        print("ваше число меньше, чем придуманное")
    elif (our_digit < your_digit):
        print("ваше число больше, чем придуманное")

def want_to_continue():
    print("""
    если вы хотите завершить угадывание, то нажмите ENTER
    если хотите продолжить, нажмите любую кнопку,кроме ENTER
    """)
    fl = input()
    return fl


main()