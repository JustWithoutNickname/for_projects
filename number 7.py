MINUTES = 60
HOURS = 3600
DAYS = 86400

seconds = int(input("введите количество секунд\t"))

if (seconds < 60):
    print(seconds, "секунд")
elif (seconds < 3600):
    print(seconds // MINUTES, "минут ",seconds % MINUTES, " секунд" )
elif (seconds < 86400):
    print(seconds // HOURS, "часов", (seconds % HOURS) // MINUTES, "минут", seconds % MINUTES, "секунд")
else:
    print(seconds // DAYS, "дней",
          (seconds % DAYS) // HOURS, "часов",
          ((seconds % DAYS) % HOURS) // MINUTES, "минут",
          seconds % MINUTES, "секунд")