#!/usr/bin/python3
import math
import sys

try:
   n = float(input())

   with open("logs.txt", "a") as f:
      f.write(f"n={n} 'test3.py'\n")

   try:
      sqrtt = math.sqrt(n)

      with open("output.txt", "a") as f:
         f.write(f"{sqrtt}\n")
   except ValueError:
      print("Квадратный корень из отрицательного числа не "
            "существует в области действительных чисел.", file=sys.stderr)
except (ValueError, EOFError):
   print("Ошибка ввода", file=sys.stderr)
