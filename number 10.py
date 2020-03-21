MONTHS_IN_YEAR = 12
def main():
    cred = get_credit()
    while (check_input(cred)):
        cred = float(input("данные не могут быть отрицательными!\t"))
    safe = get_safety()
    while (check_input(safe)):
        safe = float(input("данные не могут быть отрицательными!\t"))
    boost = get_boost()
    while check_input(boost):
        boost = float(input("данные не могут быть отрицательными!\t"))
    sum_m = month(cred, safe, boost)
    sum_y = year(sum_m)
    print("сумма расходов за месяц", format(sum_m, '.3f'))
    print("сумма расходов за год", format(sum_y, '.3f'))
def get_credit():
    return float(input("введите сумму расходов по кредиту\t"))
def get_safety():
    return float(input("введите сумму расходов на страховку\t"))
def get_boost():
    return float(input("введите сумму расходов на бензин\t"))
def check_input(argument_for_checking):
    return (argument_for_checking < 0)
def month(credit = 0, safety = 0, boost = 0):
    return credit + safety + boost
def year(summ_month):
    return summ_month * MONTHS_IN_YEAR
main()