SOSAGES = 10
BREAD = 8

number_of_participants = int(input("введите количество участников\t"))
number_of_hotdogs = int(input("введите количество хотдогов на одного участника\t"))

summ_hotdogs = number_of_participants * number_of_hotdogs
a = summ_hotdogs % SOSAGES
b = summ_hotdogs % BREAD
if (a!= 0):
    pack_sosage = summ_hotdogs // SOSAGES + 1
else:
    pack_sosage = summ_hotdogs // SOSAGES
print("необходимое количество упаковок с сосисками", pack_sosage)
if (b != 0):
    pack_bread = summ_hotdogs // BREAD + 1
else:
    pack_bread = summ_hotdogs // BREAD
print("необходимое количество упаковок с хлебом", pack_bread)
print("количество оставшихся сосисок", pack_sosage * SOSAGES - summ_hotdogs)
print("количество оставшихся хлебов", pack_bread * BREAD - summ_hotdogs)