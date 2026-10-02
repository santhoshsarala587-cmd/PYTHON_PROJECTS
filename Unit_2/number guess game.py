print("Think of a number between 1 and 50")
print("Reply only using yes or no\n")

small = 1
big = 50
steps = 0

while small != big:
    check = (small + big) // 2
    reply = input("Is your number less than or equal to " + str(check) + "? (yes/no): ").lower()
    steps += 1

    if reply == "yes":
        big = check
    elif reply == "no":
        small = check + 1
    else:
        print("Wrong input! Type only yes or no.")
        steps -= 1

print("\n Your number is", small)
print(" Total questions:", steps)