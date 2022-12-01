#!/usr/bin/python3
import random
number = random.randint(-10, 10)
<<<<<<< HEAD
if (number > 0):
    print("{} is positive".format(number))
elif (number < 0):
    print("{} is negative".format(number))
else:
    print("{} is zero".format(number))
=======
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
>>>>>>> 6141ca318647f5efced2a55be71d115d1c76ed26
