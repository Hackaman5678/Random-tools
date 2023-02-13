choice = input("To start calculator(C) Age calculator (A) Temp advise(T) and to start weight calculator(W):")

if choice.upper() == "A":
    birth_year = input("Insert birth year:")

    age = 2023 - (float(birth_year))
    print("Your age is:")
    print(age)


if choice.upper() == "W":
    weight = int(input("Enter your weight:"))
    unit = input("Kilos(K) or Lbs(L)")
    if unit.upper() == "K":
        coverted = weight / 0.45
        print("Weight in Lbs:" + str(coverted))

    else:
        coverted = weight * 0.45
        print("Weight in kgs: " + str(coverted))

if choice.upper() == "C":
    unit = input("Plus(P) Minus(M) Divide(D) or Times(T):  ")
    if unit.upper() == "P":
        first = float(input("first:"))
        print("Plus")
        second = float(input("Second:"))

        sum = float(first) + float(second)

        print(sum)

    if unit.upper() == "M":
        first = float(input("first:"))
        print("Minus")
        second = float(input("Second:"))

        sum = float(first) - float(second)

        print(sum)
    if unit.upper() == "T":
        first = float(input("first:"))
        print("Times")
        second = float(input("Second:"))

        sum = float(first) * float(second)

        print(sum)
    if unit.upper() == "D":
        first = float(input("first:"))
        print("Divide")
        second = float(input("Second:"))

        sum = float(first) / float(second)

        print(sum)


if choice.upper() == "T":
    temp = input("Enter temp:")
    if temp >= "25":
        print("Its a hot day drink about 2L of water")
    if temp == "21":
        print("Its a mildy hot day drink about 1 to 1.5 liters  ")

    if temp == "22":
        print("Its a mildy hot day drink about 1 to 1.5 liters  ")

    if temp == "23":
        print("Its a mildy hot day drink about 1 to 1.5 liters  ")

    if temp == "24":
        print("Its a mildy hot day drink about 1 to 1.5 liters  ")

    if temp <= "15":
        print("Its a cold day dress warm and drink water")