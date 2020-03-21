def main():
    flag = True
    while flag:
        try:
            n = int(input("введите количество элементов в списке\t"))
            flag = False
        except ValueError:
            print("нужно целое число!!!")
        else:
            if (n <= 0) or (n > 100):
                print("введено ну очень большое число (ну или слишком маленькое)")
                flag = True
    digits = input_list(n)
    print("сумма всех элементов списка: ", summ(digits))
def input_list(n):
    yr_list = []
    for i in range(n):
        flag = True
        while flag:
            try:
                item = float(input("введите числовое значение\t"))
                flag = False
            except ValueError:
                print("нужно числовое значение!!!")
        yr_list.append(item)
    return  yr_list
def summ(yr_list):
    summa = 0
    for item in yr_list:
        summa += item
    return  summa

main()