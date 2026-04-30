hours = input("enter number of hours worked:")
hrs = float(hours)
rate = input("enter rate:")
rt = float(rate)
if hrs <= 40:
    pay = hrs * rt
else:
    pay = 40 * rt + (hrs - 40) * rt * 1.5
print("pay:", pay)