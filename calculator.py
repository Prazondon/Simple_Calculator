def cal():
    print("enter the choice. \n 1 for addition. \n 2 for substraction. \n 3 for multiplication. \n 4 for division.")
    
def add_numbers(a,b):

    return a+b

def substraction (a,b):
    result = a - b
    return result

def multiplication(a,b):
    result = a * b
    return result

def division (a,b):
    result = a /b 
    return result

while True:
    cal()
    choice = int(input("enter your choice"))
    num1 = int(input("enter the number"))
    num2 = int(input("enter the number"))


    if choice == 1:
        addition = add_numbers(num1, num2)
        print(addition)


    elif choice == 2:
        substaction1 = substraction(num1, num2)
        print(substaction1)

    elif choice == 3:
        multi = multiplication(num1, num2)
        print(multi)

    elif choice == 4:
        div = division(num1, num2)
        print(div)

    elif choice == 5:
        print("you have exited ")
        break

    else:
        print("invalid number")







