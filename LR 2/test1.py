#!/usr/bin/python3
import sys

def see_you():
    with open("names.txt", "r") as f:
        for line in f:
            name = line.strip()
            if not name:
                continue
            if not name[0].isupper():
                print(f"Error: Name '{name}' needs to start in uppercase!",
                      file=sys.stderr)
            elif not name.isalpha():
                print(f"Error: Name '{name}' contains invalid characters!",
                      file=sys.stderr)
            else:
                print(f"Nice to see you {name}!")

def names():
    try:
        while True:
            name = input("Hey, what's your name?\n")
            if not name[0].isupper():
                print(f"Error: Name '{name}' needs to start in uppercase!",
                      file=sys.stderr)
            elif not name.isalpha():
                print(f"Error: Name '{name}' contains invalid characters!",
                      file=sys.stderr)
            else:
                print(f"Nice to see you {name}!")
    except KeyboardInterrupt:
        print("\nGoodbye!")

if __name__ == "__main__":
    if not sys.stdin.isatty():
        see_you()
    else:
        names()
