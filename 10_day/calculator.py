def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = int(input("Enter a number: "))
op = input("""Choose an operator from the options below
           +
           -
           *
           /
""")
num2 = int(input("Enter second number: "))

def calculator(num1, num2):
    if op == '+':
        ans = num1 + num2
    elif op == '-':
        ans = num1 - num2
    elif op == '*':
        ans = num1 * num2
    elif op == '/':
        ans = int(num1 / num2)
    else:
        ans = "Wrong operation"
    return ans

print(calculator(num1, num2))
    
continue_op = True

while continue_op:
    another_op = input("Do you want to continue calculating? \"Yes\" or \"No\" ").lower()
    if another_op =="no":
        continue_op = False
    else:  
        num1 = calculator(num1, num2)
        op = input("Choose operation: ")
        num2 = int(input("Enter second number: "))
        print(calculator(num1, num2))