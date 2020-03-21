SQUERE = 10
LITRES = 5
HOURS = 8
MINUTES = 60
MONEY_HOUR = 2000
MONEY_MINUTE = 33.3
def main():
    sq = get_squere()
    cost_paint =get_paint_cost()
    cans = paint_cans(sq)
    print(cans, "\tбанок краски потребуется для покраски помещения")
    hours, minutes = working_hours(sq)
    print("рабочим понадосится", hours, "часов", format(minutes, '.1f'), "минут")
    paint_costs = cost_p(cans, cost_paint)
    print("стоимость краски составит\t", paint_costs)
    work_costs = cost_of_working(hours, minutes)
    print("стоимость покраски составляет\t", format(work_costs, '.2f'))
    print("стоимость всей покраски заданной площади с учетом стоимости 5литровой " 
          "упаковки краски(краска + работа)\t", sum_of_working(paint_costs,work_costs))
def get_squere():
    return float(input("введите квадратные метры, которые необходимо покрасить\t"))
def get_paint_cost():
    return float(input("введите стоимость 5 литровой упаковки\t"))
def paint_cans(sq_metres):
    if (sq_metres % SQUERE != 0):
        return (sq_metres // SQUERE) + 1
    else:
        return  (sq_metres // SQUERE)
def working_hours(sq_metres):
    hour = (sq_metres * HOURS / SQUERE) // 1
    minutes = ((sq_metres * HOURS/ SQUERE) % 1) * MINUTES
    return hour, minutes
def cost_p(cans, cost_paint):
    return cans * cost_paint
def cost_of_working(hours, minutes):
    return hours * MONEY_HOUR + minutes * MONEY_MINUTE
def sum_of_working(paint_costs, work_costs):
    return paint_costs + work_costs
main()