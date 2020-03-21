import turtle
import math
import random
print("""
ПРИВЕТСТУВУЮ ВАС В ИНТЕЛЛЕКТУАЛЬНОЙ ИГРЕ 'ПОПАДИ В ЦЕЛЬ'!
ВАША ЗАДАЧА ПОПАСТЬ В ОБВЕДЕННУЮ ОБЛАСТЬ (КВАДРАТ ИЛИ ПРЯМОУГОЛЬНИК)!
НИЖЕ ВАМ ДАНЫ КООРДИНАТЫ (ВНИМАНИЕ!) ЦЕНТРА МАСС ОБЛАСТИ
НЕОБХОДИМО ЗАДАТЬ УГОЛ В ПРЕДЕЛАХ [0 : 360)
                  РАССТОЯНИЕ
ПОПУТНО БУДУТ ВЫВОДИТСЯ ПОДСКАЗКИ, ЕСЛИ ВЫ НЕ ПОПАДЕТЕ
ЖЕЛАЮ УДАЧИ!:)

                       |
А ВОТ И ВАШЕ ЗАДАНИЕ   |
                       V
""")
#именованные константы
SETUP_WIDTH = 480
SETUP_LENGTH = 640
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270
TARGET_WIDTH = 25
TARGET_LENGTH = 25

#основная программа
turtle.setup(SETUP_LENGTH, SETUP_WIDTH)
turtle.speed(0)
turtle.penup()
turtle.hideturtle()
target_beginX = random.randint(-200,201)
target_beginY = random.randint(-200, 201)
print("координата по оси X:", target_beginX)
print("координата по оси Y:", target_beginY)
if (target_beginY == 0 and target_beginX < 0):
    target_angle = 180
elif (target_beginY == 0 and target_beginX >= 0):
    target_angle = 0
elif (target_beginX >= 0 and target_beginY > 0):
    target_angle = math.degrees(math.atan(target_beginY/target_beginX))
elif (target_beginY < 0 and target_beginX >= 0):
    target_angle = math.degrees(math.atan(target_beginY / target_beginX)) + 360
else:
    target_angle = math.degrees(math.atan(target_beginY / target_beginX)) + 180
    #print(target_angle)
target_distance = math.sqrt((target_beginX + TARGET_LENGTH / 2) ** 2 + (target_beginY +TARGET_WIDTH / 2) ** 2)
turtle.pencolor("red")
turtle.goto(target_beginX, target_beginY)
turtle.dot()
turtle.goto(target_beginX - TARGET_LENGTH/2, target_beginY - TARGET_WIDTH/2)
turtle.pendown()
for i in range(4):
    turtle.forward(TARGET_LENGTH)
    turtle.left(90)
turtle.penup()
turtle.speed(4)
turtle.goto(0, 0)
turtle.showturtle()
turtle.pencolor("green")
#теперь будем пускать луч
fl = True
while (fl):
    turtle.setheading(0)
    angle = float(input("введите угол в градусах (<360  и >=0)\t"))
    while (angle > 360 or angle < 0):
        angle = float(input("введите угол в градусах (<360  и >=0)\t"))
    turtle.goto(0, 0)
    turtle.setheading(angle)
    distance = float(input("введите дистанцию, на которую передвинется черепашка\t"))
    #my_turtle.speed(4)
    turtle.forward(distance)
    if (turtle.xcor() >= target_beginX - TARGET_LENGTH/2 and
        turtle.ycor() >= target_beginY - TARGET_WIDTH/2 and
        turtle.xcor() <=target_beginX + TARGET_LENGTH/2 and
        turtle.ycor() <= target_beginY + TARGET_WIDTH/2):
            print("ПОЗДРАВЛЕНИЯ! ВЫ ПОПАЛИ!!!")
            fl= False
    elif (angle > target_angle and distance < target_distance):
        print ("возьмите угол поменьше, а дистанцию побольше")
    elif (angle < target_angle and distance > target_distance):
        print("возьмите угол побольше, а дистанцию поменьше")
    elif (angle > target_angle and distance > target_distance):
        print ("возьмите угол и дистанцию поменьше")
    elif (angle < target_angle and distance < target_distance):
        print ("возьмите угол и дистанцию побольше")
    elif (angle == target_angle and distance < target_distance):
        print("с углом расправились, осталось с дистанцией: возьмите побольше")
    elif (angle == target_angle and distance > target_distance):
        print("с углом расправились, осталось с дистанцией: возьмите поменьше")
    elif (distance == target_distance and angle > target_angle):
        print("с дистанцией расправились, осталось с углом: возьмите поменьше")
    elif (distance == target_distance and angle < target_angle):
        print("с дистанцией расправились, осталось с углом: возьмите побольше")
    #my_turtle.speed(0)
turtle.getscreen()._root.mainloop()
