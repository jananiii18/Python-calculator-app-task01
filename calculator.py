Python-calculator-app #code
def show_operations():
    print("1.Addition")
    print("2.Subraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit!")
    print("Which one would you like to choose?")

def input_numbers():
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    return a,b
    
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
       return a
    elif a == 0:
        return 0
    else:
        return a/b
    
def main_function():
    while True:
        show_operations()
        user_input = int(input("Enter an operation from 1 to 5: "))
        if user_input == 5:
            print("Good bye!")
            break
        elif user_input in[1,2,3,4]:
            a,b = input_numbers()
            if user_input == 1:
               print("Result:",add(a,b))
            elif user_input == 2:
               print("Result:",sub(a,b))
            elif user_input == 3:
               print("Result:",mul(a,b))
            elif user_input == 4:
               print("Result:",div(a,b))
        else:
            print("Invalid one")
            
main_function()
