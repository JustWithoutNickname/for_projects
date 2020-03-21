MARK_A = 90
MARK_B = 80
MARK_C = 70
MARK_D = 60
def main():
    n = int(input("введите количество оценок за семестр\t"))
    while check_input_amount(n):
        n = int(input("введите положительное количество оценок, иначе смысл считать?\t"))
    marks = data(n)
    print("ваш средний балл равен", format(mid_ball(marks, n), '.2f'))
    determine_grade((marks))
def data(n = 0):
    marks = []
    for i in range(n):
        mark = int(input("введите очередную оценку\t"))
        while check_input_mark(mark):
            mark = int(input("не пытайтесь обмануть систему! введите правильную оценку!\t"))
        marks.append(mark)
    return marks
def mid_ball(marks, n):
    mball = 0
    for item in marks:
        mball += item
    mball /= n
    return mball
def determine_grade(marks):
    for item in marks:
        if item >= MARK_A:
            print(item,": A", sep = '')
        elif item >= MARK_B:
            print(item, ": B", sep = '')
        elif item >= MARK_C:
            print(item, ": C", sep = '')
        elif item >= MARK_D:
            print(item, ": D", sep = '')
        else:
            print("очень жаль, но ваша оценка только F, вам необходимо пересдать этот предмет")
def check_input_amount(n):
    return n <= 0
def check_input_mark(mark):
    return (mark <= 0) or (mark > 100)
main()