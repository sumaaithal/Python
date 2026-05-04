count = 0
tot = 0.0
while True:
    sval = input("Enter a number:")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    count = count + 1
    tot = tot + fval
print(count, tot, tot/count)
print("All done")