#!/usr/bin/python3
import random

A = random.randint(-10, 10)
print(A)

with open("logs.txt", "a") as f:
    f.write(f"A={A} 'test1.py'\n")
