salary = float(input("What's the current salary? "))
increaseRate = float(input("What's the increase rate? (in %) "))

finalSalary = salary + salary * (increaseRate/100)
print("Your new salary, after a increase of {}% is: ${}!".format(increaseRate, format(finalSalary, ".2f")))