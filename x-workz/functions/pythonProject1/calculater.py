def userInput():
    first_input=int(input("enter the first name:"))
    second_input=int(input("enter the second name:"))
    return first_input, second_input

def add(a=0,b=0):
    return a+b

def sub(a=0,b=0):
    return a-b

def mul(a=0,b=0):
    return a*b

print("KAI MUGIDU OLAGE BANNI")
while True:
    print("select the choose:\n 1:add\n 2:sub\n 3:mul\n 4:stop")
    choose=int(input("enter the choose:"))

    if choose==1:
        x,y=userInput()
        print(f"addition of two number:({add(x,y)}")

    elif choose==2:
        x, y = userInput()
        print(f"substration of two number:({sub(x, y)}")

    elif choose == 3:
        x, y = userInput()
        print(f"multiplication of two number:({mul(x, y)}")

    elif choose == 4:
        print("BANDIDAKKE DHANYAVADAGALU")
        break