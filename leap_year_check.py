
year = int(input("Which year do you want to check? "))


if year % 4 == 0:
    if year % 100 == 0:
        print("This is leap year.")
    else:
        if year % 400:
            print("This is leap year.")
        else:
            print("This is not leap year.")
else:
    print("This is not leap year.")