year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print(f"Year {year} is a leap year.")
    else:
        print(f"Year {year} is not a leap year.")
else:
    print(f"Year {year} is not a leap year.")
