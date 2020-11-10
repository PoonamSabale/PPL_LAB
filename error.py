a = 5
b = 2
c = 10


x = int(input("Enter no greater than zero "))
if x < 0:
  raise Exception("Sorry, no numbers below zero")


try:
  print(a/b)
  print(c)
  d = int(input("Enter a number "))
  print(d)
  f = open("f1.txt")

except ZeroDivisionError:
  print("Can not divide by zero")

except NameError:
  print("Variable is not defined")

except ValueError:
  print("Invalid input")

except FileNotFoundError:
  print("File does not exist")

else:
  print("Nothing went wrong")

finally:  
  print("Finished")
