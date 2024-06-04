Birth_year = int(input("Birth year :"))
year = int(input("year :"))
Month_now = int(input("month now :"))
Month_birth = int(input("month of birth: "))
Month = Month_now - 12 + Month_birth
Result = year - Birth_year
print(f"you are,{Result} years old and {Month} months old")
