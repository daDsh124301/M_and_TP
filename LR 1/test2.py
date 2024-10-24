#!/usr/bin/env python3
import random

a = int(input())
print(f"A = {a}")
b = random.randint(-10, 10)
print(f"B = {b}")
if b == 0: 
    print("Error")
else:         
   result = a / b
   print(f"A / B = {result}")