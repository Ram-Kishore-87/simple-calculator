n=2
while True:
    principle = float(input("Enter the Principle amount:$ "))
    if principle <= 0:
        principle =float(input("Principle amount cant be negative ,please try again (%): "))

    else:
        break

while True:
    rate = float(input("Enter the annual interest rate : "))
    if rate <= 0:
        rate = float(input("The annual interest rate vant br nrgativr ,Please try again (%): "))
    else:
        break
while True:
    time = float(input("Enter the tenure (in years) : "))
    if time <= 0:
        time = float(input("The time (in years) cant be negative ,please try again (%): : "))
    else:
        break
r=rate/100
total=principle*pow((1+r/n),n*time)
print(f"The Compound intrest for the principle amount {principle} over the time of{time} years is :{total:.2f}")