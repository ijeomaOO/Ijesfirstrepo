num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

def calc(num1, op, num2):
    if op == "+":
        return(num1 + num2)
    elif op == "-":
        return(num1 - num2)  
    elif op == "*":
        return(num1 * num2)
    elif op == "/":
        return(num1 / num2)
    else: 
        return("Invalid Operation")
    
print(calc(num1, op,num2))