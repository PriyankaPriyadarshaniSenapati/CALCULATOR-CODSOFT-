def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error! can't divide by zero, please change the denominator"
    else:
        return x/y

def calculaor():
    print("SIMPLE CALCULATOR")
    print("OPERATIONS:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter the operation number (1/2/3/4) or 'q' to quit : ")
        if choice=='q':
            print("Exiting the calculator")
            break
        if choice not in ['1','2','3','4']:
            print("Invalid input! please enter  a valid operation number")
            continue

        try:
            num1=float(input("Enter the first number : "))
            num2=float(input("Enter the second number : "))
        except ValueError:
            print("Invalid input! please enter numeric values")
            continue

        if choice == '1':
            result = add(num1,num2)
            print("the result of addition of ",num1," with ",num2," is ",result)
        elif choice == '2':
            result = subtract(num1,num2)
            print("the result of subtraction of ",num2," with ",num1," is ",result)
        elif choice == '3':
            result = multiply(num1,num2)
            print("the result of multiplication of ",num1," with ",num2," is ",result)
        elif choice == '4':
            result = divide(num1,num2)
            print("the result of division of ",num1," by ",num2,"is",result)

if __name__=="__main__":
    calculaor()
            
            