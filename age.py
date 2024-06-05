Birth_year = int(input("Birth year :"))
year = int(input("year :"))
Month_now = int(input("month now :"))
Month_birth = int(input("month of birth: "))
Month = Month_birth - Month_now
Result = year - Birth_year
Late = int(input("12,11,10,9,8,0 if you have a late birth-day please enter it again if not please press 0 :\n"));
if Month_birth == Late:
        while True:
                Result - 1
print(f"you are,{Result} years old and {Month} months old")

