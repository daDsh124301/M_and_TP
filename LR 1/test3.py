#!/usr/bin/env python3
import math

n = float(input())
sqrtt = math.sqrt(n)
with open("output.txt", "s") as f:
   f.write(str(sqrtt) + "\n")