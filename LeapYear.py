year = int(input("Enter the year: "))
if year % 4 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')




def leap(year):
    if (year % 4) == 0:
        return True
    else:
        return False
year = int(input())
print(leap(year))
