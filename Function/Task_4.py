def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

result = simple_interest(p, r, t)

print("Simple Interest:", result)