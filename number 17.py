import random
#random.seed(20)
def main():
    file = open(r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/file200.txt', 'w')
    n = input_amount()
    for i in range(n):
        item = random.randint(1, 500)
        file.write(str(item) + '\n')
    file.close()
    required_file = require_for_file()
    summa, kolvo = output_from_the_file(required_file)
    print("сумма сгенерированных чисел: ", summa, " количество сгенерированных чисел: ", kolvo)

def require_for_file():
    name_file = input('введите название файла c расширением\t')
    flag = True
    while flag:
        try:
            opened_file = open(r'/Users/macbookair/Desktop/MyPythonStading/files/all_files/' + name_file, 'r')
            flag = False
        except IOError:
            print("такого файла в папке all_files нет:(")
            name_file = input("попытайтесь снова\t")
    return opened_file
def output_from_the_file(opened_file):
    item = opened_file.readline()
    amount = 0
    summ = 0
    while item:
        amount += 1
        item = item.rstrip('\n')
        print(amount, 'число: ', int(item), sep = '')
        summ += int(item)
        item = opened_file.readline()

    opened_file.close()
    return summ, amount
def input_amount():
    flag = True
    while flag:
        try:
            n = int(input("введите количество чисел\t"))
        except ValueError:
            print("необходимо именно ЦЕЛОЕ число")
        else:
            if (n > 0) and (n < 501):
                flag = False
    return n

main()