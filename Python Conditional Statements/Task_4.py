balance = int(input("Enter Your Balance:"))
withdrawal=int(input("Enter Your Withdrawal amount:"))

if withdrawal <=balance:
    print("Withdrawal successfull")
    balance = balance-withdrawal
    print("yopur remaining balance is:",balance)
else:
    print("Insuffficient balance")