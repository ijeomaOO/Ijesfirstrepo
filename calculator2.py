selection = int(input("What function do you want to perform? \nType the number for the operation you wish to perform \n 1 for Addition \n 2 for Subtraction \n 3 for Multiplication \n 4 for Division \n "))
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
sumNum = num1 + num2
subnum = num1 - num2
mulNum = num1 * num2
divnum = num1 / num2

if selection == 1:
    print(sumNum)
elif selection == 2:
    print(subnum)
elif selection == 3:
    print(mulNum)
else:
    print(divnum)
    
    