num1 = float(input("Enter a number: "))

op_valid = True
while op_valid:
    op = input("""Choose an operator from the options below
    +
    -
    *
    /
""")
    if op == '+' or op == '-' or op == '*' or op == '/':
        op_valid = False
    else:
        print('Wrong operation')
        
num2 = float(input("Enter second number: "))

def calculator(num1, num2):
    if op == '+':
        ans = num1 + num2
    elif op == '-':
        ans = num1 - num2
    elif op == '*':
        ans = num1 * num2
    elif op == '/':
        ans = num1 / num2

    ans = round(ans, 2)
    print(f"{num1} {op} {num2} = {ans}")
    return ans

answer = calculator(num1, num2)
continue_op = True

while continue_op:
    op_check = True
    another_op = input(f"Do you want to continue calculating with {answer}? \"Yes\" or \"No\": ").lower()
    if another_op == "no":
        continue_op = False
        print("Thank you!!!")
    elif another_op == "yes":  
        num1 = answer
        while op_check:
            op = input("Choose another operation: ")
            if op == '+' or op == '-' or op == '*' or op == '/':
                op_check = False
            else:
                print('Wrong operation')
                op
        num2 = float(input("Enter next number: "))
        answer = calculator(num1, num2)
    else:
        another_op