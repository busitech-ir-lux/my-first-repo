#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
	print(f"{number} is POSITIVE")
elif number < 0:
	print(f"{number} is NEGATIVE")
else: print(f"{number}  is ZERO")
