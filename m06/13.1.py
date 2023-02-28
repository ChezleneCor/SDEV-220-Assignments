from datetime import date

t = open ("today.txt" , "w")

today = date.today()

format = "%A, %B %d, %Y,"

today = today.strftime(format)

for s in today:
    t.write(s)
