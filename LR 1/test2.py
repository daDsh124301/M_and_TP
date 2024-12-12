#!/usr/bin/python3
import random
import sys

try:
    a = int(input())
    b = random.randint(-10, 10)

    with open("logs.txt", "a") as f:
        f.write(f"A={a} B={b} 'test2.py'\n")

    result = a / b
    print(result)
except ZeroDivisionError:
    print("Деление на ноль", file=sys.stderr)
except ValueError:
    print("Ошибка ввода", file=sys.stderr)
