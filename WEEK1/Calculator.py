print("Simple Calculator")
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
op = input("Enter operation (* / + -): ")

def switch(op):
    if op == "+":
        add = num1 + num2
        return add
    elif op == "/":
        divides = num1 / num2;
        return divides
    elif op == "*":
        multiply = num1 * num2;
        return multiply
    elif op == "-":
        minus = num1 - num2;
        return minus
    else:
        print("ENTER VALID OPERATIONS!")
    
print("Total is:",switch(op)) 

