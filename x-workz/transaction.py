balance=10000
credit=int(input("enter amount credit:"))
if credit < balance:
    pass
else:
    debit=int(input("enter amount debit:"))
if debit > balance:
    balance+=credit
    print(f"transaction complete remaing balance debits():{balance}")
    balance-=debit
else:
    print(f"remaing credit balance():{balance}")
ifelse:
    print(f"remaing debit balance():{balance}")



