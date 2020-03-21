import os
def main():
    n = input_amount()
    our_file = open(r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/gholf-sportsmen.txt', 'w')
    for i in range(n):
        our_file = recording(our_file)
    our_file.close()
    print("данные о спортсменах по гольфу записаны в файл gholf-sportsmen.txt")
    print("""
                МЕНЮ
        что вы хотели бы сделать?    
    print_all   показать всех спортсменов
    add         добавить спортсмена
    delete      удалить спротсмена
    change      изменить информацию о спротсмене
    exit        выход из программы
    """)
    choice = input("ваш выбор:\t")
    while (choice.lower() != "exit"):
        if (choice.lower() == "print_all"):
            print_all()
            print("""
                            МЕНЮ
                    что вы хотели бы сделать?    
                print_all   показать всех спортсменов
                add         добавить спортсмена
                delete      удалить спротсмена
                change      изменить информацию о спротсмене
                exit        выход из программы""")
            choice = input("ваш выбор:\t")
        elif (choice.lower() == "add"):
            our_file = open(r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/gholf-sportsmen.txt', 'a+')
            our_file = recording(our_file)
            print("Информация о игроке записана в файл gholf-sportsmen.txt")
            our_file.close()
            print("""
                                        МЕНЮ
                                что вы хотели бы сделать?    
                            print_all   показать всех спортсменов
                            add         добавить спортсмена
                            delete      удалить спротсмена
                            change      изменить информацию о спротсмене
                            exit        выход из программы""")
            choice = input("ваш выбор:\t")
        elif (choice.lower() == "delete"):
            delete()
            print("""
                                        МЕНЮ
                                что вы хотели бы сделать?    
                            print_all   показать всех спортсменов
                            add         добавить спортсмена
                            delete      удалить спротсмена
                            change      изменить информацию о спротсмене
                            exit        выход из программы""")
            choice = input("ваш выбор:\t")
        elif (choice == "change"):
            changing()
            print("""
                                        МЕНЮ
                                что вы хотели бы сделать?    
                            print_all   показать всех спортсменов
                            add         добавить спортсмена
                            delete      удалить спротсмена
                            change      изменить информацию о спротсмене
                            exit        выход из программы""")
            choice = input("ваш выбор:\t")
        else:
            print("""такой команды нет!!!
            
                                        МЕНЮ
                                что вы хотели бы сделать?    
                            print_all   показать всех спортсменов
                            add         добавить спортсмена
                            delete      удалить спротсмена
                            change      изменить информацию о спротсмене
                            exit        выход из программы""")
            choice = input("ваш выбор:\t")

def input_amount():
    flag = True
    while flag:
        try:
            n = int(input("введите количество игроков в гольф\t"))
            flag = False
        except ValueError:
            print("необходимо целое число игроков")
        else:
            if (n <= 0) or (n > 200):
                flag = True
    return n
def recording(opened_file):
    name = input("введите имя спортсмена\t")
    name = name.capitalize()
    flag = True
    while flag:
        try:
            scores = float(input("введите количество очков у игрока (по 100бальной шкале)\t"))
            flag = False
        except ValueError:
            print("необходимо вещественное или целое количество очков")
        else:
            if (scores < 0) or (scores > 100):
                print("такого количесва очков быть не может!")
                flag = True
    opened_file.write(name + '\n')
    opened_file.write(str(scores) + '\n')
    return opened_file
def print_all():
    opened_file = open(r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/gholf-sportsmen.txt', 'r')
    name = opened_file.readline()
    while name:
        scores = opened_file.readline()
        scores = float(scores)
        name = name.rstrip('\n')
        print('Игрок', name, 'набрал', scores, 'очков' )
        name = opened_file.readline()
    opened_file.close()

def delete():
    opened_file = open(r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/gholf-sportsmen.txt', 'r')
    add_file = open(r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/add_file.txt', 'w')
    search = input("введите имя спортмена, которого хотите удалить из списка\t")
    search = search.capitalize()
    name = opened_file.readline()
    flag = True
    while name:
        scores = float(opened_file.readline())
        name = name.rstrip('\n')
        if (name == search):
            flag = False
        else:
            add_file.write(name + '\n')
            add_file.write(str(scores) +'\n')
        name = opened_file.readline()
    if flag == True:
        print('введенного вами имени в файле не нашлось')
    add_file.close()
    opened_file.close()
    os.remove(r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/gholf-sportsmen.txt')
    os.rename(r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/add_file.txt',
              r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/gholf-sportsmen.txt')
def changing():
    opened_file = open(r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/gholf-sportsmen.txt', 'r')
    add_file = open(r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/add_file.txt', 'w')
    search = input("введите имя игрока, информацию о котором вы хотели бы изменить\t")
    search = search.capitalize()
    flag = True
    name = opened_file.readline()
    while name:
        scores = float(opened_file.readline())
        name = name.rstrip('\n')
        name = name.capitalize()
        if name == search:
            while flag:
                thing_to_change = input("что хотите поменять у игрока с именем " + name +
                                        "?\n('имя' или 'очки' или введите что угодно, если менять больше ничего не надо)\t")
                thing_to_change = thing_to_change.lower()
                if thing_to_change == 'имя':
                    name = input('введите новое имя\t')
                elif thing_to_change == 'очки':
                    while flag:
                        try:
                            scores = float(input("введите количество очков у игрока (по 100бальной шкале)\t"))
                            flag = False
                        except ValueError:
                            print("необходимо вещественное или целое количество очков")
                        else:
                            if (scores < 0) or (scores > 100):
                                print("такого количесва очков быть не может!")
                                flag = True
                    flag = True
                else:
                    flag = False
            add_file.write(name + '\n' + str(scores) + '\n')
        else:
            add_file.write(name + '\n' + str(scores) + '\n')
        name = opened_file.readline()
    if flag == True:
        print("игроков с таким именем не оказалось")
    os.remove(r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/gholf-sportsmen.txt')
    os.rename(r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/add_file.txt',
              r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/gholf-sportsmen.txt')
main()

