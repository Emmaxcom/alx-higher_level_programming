#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
<<<<<<< HEAD
if(number < 0):
    lastDigit = int(str(number)[-1]) * -1
else:
    lastDigit = int(str(number)[-1])
first = "Last digit of "
last = " and is less than 6 and not 0"
if(lastDigit > 5):
    print(first + "{} is {} and is greater than 5".format(number, lastDigit))
elif(lastDigit == 0):
    print(first + "{} is {} and is 0".format(number, lastDigit))
else:
    print(first + "{} is {}".format(number, lastDigit) + last)
=======
if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10
if lastdigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastdigit))
elif lastdigit < 6 and lastdigit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lastdigit))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
>>>>>>> 6141ca318647f5efced2a55be71d115d1c76ed26
