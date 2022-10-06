age = 0

age = int(input("How old are you?"))
   
if age >= 17:
    print("You can watch an R rated movie alone.")
elif age >= 13:
    print("You can watch a Pg-13 movie alone.")
elif age >= 5:
    print("you can watch a G or PG movie alone.")
else:
  print("OH NO you are too young to watch most movies, try again when you are much older 💀")

