hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
# usual rate per hour for up to 40 hours
if h <= 40.00:
    pay = h * r
else:
# 1.5 rate per hour for hours worked above 40 hours
    i = h - 40
    pay = (r * 40) + (r * 1.5 * i)
print(pay)
