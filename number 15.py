import random

STONE = "камень"
PAPER = "бумага"
SCISSORS = "ножницы"
def main():
    print("""
ПРИВЕТСТВУЕМ в игре \"камень-ножницы-бумага\"
вам необходимо ввести один из вариантов: камень, ножницы или бумага
камень бьёт ножницы, бумага заворачивает камень, ножницы режут бумагу
в случае ничьи придется выбирать снова
    """)
    flag = True
    while flag:
        our_choice = random.randint(1, 3)
        our_choice = transform(our_choice)
        your_choice = input("ваш выбор: ножницы, камень или бумага?\t")
        your_choice = your_choice.lower()
        while (your_choice != SCISSORS) and (your_choice != STONE) and (your_choice != PAPER):
            your_choice = input("вводите некорректные данные! ")
        flag = checking_answer(your_choice, our_choice)
        if flag == False:
            your_choice = input("хотите ли сыграть еще? если да, введите \"да\"")
            if (your_choice.lower() == "да"):
                flag = True

def checking_answer(answ, our_choice):
    if ((answ == STONE) and (our_choice == PAPER)) or \
            ((answ == SCISSORS) and (our_choice == STONE)) or \
            ((answ == PAPER) and (our_choice == SCISSORS)):
        print("Ваш ответ: " + answ + "; компьютер загадал: " + our_choice)
        print("увы, но вы проиграли")
        return False
    elif ((answ == PAPER) and (our_choice == STONE)) or \
            ((answ == STONE) and (our_choice == SCISSORS)) or \
            ((answ == SCISSORS) and (our_choice == PAPER)):
        print("Ваш ответ: " + answ + "; компьютер загадал: " + our_choice)
        print("поздравляем, вы выиграли!")
        return False
    else:
        print("ого, у вас ничья! Вы загадли " + answ)
        return True

def transform(our_choice):
    if our_choice == 1:
        return "ножницы"
    elif (our_choice == 2):
        return "камень"
    else:
        return  "бумага"

main()