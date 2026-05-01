def computepay(h,r):
    if h <= 40:
        return (h*r)
    else:
        return (h*r)+((h-40)*(r*0.5))
hours = input("please enter hours workd:")
hours = int(hours)
rate = input("please enter the rate:")
rate = float(rate)

p = computepay(hours, rate)
print("pay is:",p)
