
percents = float(input("введите количество процентов "))
while (percents <0 or percents > 100):
    percents = float(input("введите количество процентов "))
percents= 1 + percents/100

price = float(input("введите стоимость в семестр "))
while(price < 0):
    price = float(input("введите стоимость в семестр "))
summ = 0
for i in range(5):
    summ += price * 2
    price *= percents
print("Всего необходимо будет заплатить ", format(summ, ',.2f'), " рублей")

