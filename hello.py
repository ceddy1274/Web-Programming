try:
    n = int(input("Number: "))

    if n > 0:
        print("n is positive")
    elif n < 0:
        print("n is negative")
    else:
        print("n is 0")
except ValueError:
    print("not a number")