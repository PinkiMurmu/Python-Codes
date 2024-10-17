'''list=[10,11,12,13,14,15]
print(len(list))
x=input("Enter a number:")
y=input("Enter another number:")
try:
    if x>y:
        print(x,"is greater")
    elif x<y :
        print(x," is smaller")
except:
    print("both are equal")'''


import calendar

# Replace 2024 with the desired year
year = 2024

# Print the full calendar for the specified year
cal = calendar.TextCalendar(calendar.SUNDAY)
full_year = cal.formatyear(year, 2, 1, 1, 3)
print(full_year)
