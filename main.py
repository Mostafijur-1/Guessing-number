
for z in range(5):
    import random

    a = int(input("Enter a random Num(between 0 to 10): "))
    b = random.randrange(0, 10)

    if a < 0 or a > 10:
        print("It's not a valid number. Please Enter a number between 0 to 10")

    if a==b:
        print("You have won")

    else:
        print("You have lost , the random number was",b)


else:
  print("Finally finished!")

