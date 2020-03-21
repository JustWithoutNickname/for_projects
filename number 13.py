import  math
def main():
    n = int(input("введите дапазон значений, где необходимо вывести все простые числа\t"))
    if (n >= 2):
        print(1, 2, end = ' ')
        k = 2
        for i in range(3, n + 1, 2):
            j = 1
            while (j <= math.sqrt(i)):
                fl = True
                if (j != 1) and (i % j == 0):
                    fl = False
                    j += 1
                    break
                else:
                    j += 1
            if (fl == True):
                if (k % 10 == 0):
                    print()
                print(format(i, 'd'), end = ' ')

                k += 1
    elif (n == 1):
        print(1)


main()
