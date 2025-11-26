balance=10000
debit=int(input("enter amount debit:"))
if(debit<=balance):
    balance-=debit
    print(f"transaction complete remaing balance:{balance}")
else:
    print("don't have balance!")