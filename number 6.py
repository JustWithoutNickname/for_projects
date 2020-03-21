GRAMMS = 100
PRICE_1 = 150
PRICE_2 = 300
PRICE_3 = 400
PRICE_4 = 475
our_bag = float(input("введите вес сумки в граммах\t"))
while (our_bag <=0):
    our_bag = float(input("введите вес сумки в граммах, больший нуля\t"))
if our_bag <= 200:
    price = (our_bag // 100) * PRICE_1 + ((our_bag % 100) / 100 )* PRICE_1
elif our_bag <= 600:
    price = (our_bag // 100) * PRICE_2 + ((our_bag % 100) / 100 )* PRICE_2
elif our_bag <= 1000:
    price = (our_bag // 100) * PRICE_3 + ((our_bag % 100) / 100 ) * PRICE_3
else:
    price = (our_bag // 100) * PRICE_4 + ((our_bag % 100) / 100 ) * PRICE_4
print("итоговая цена перевозки", format(price, '.2f'), sep=': ')