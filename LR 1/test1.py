#!/usr/bin/env python3
import random
try:
    A = random.randint(-10, 10)
    print(A)
    
except ValueError as e:
    print(e)
    with open("errors.txt", "A") as f:
        print(e, file=f)