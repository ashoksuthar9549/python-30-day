def calculate():
    # Write your basic CLI calculator script here
    # It should take user input for numbers and an operation (+, -, *, /)
    # and print the result.
    def add(a, b):
        return a+b

    def sub(a, b):
        return a-b
        
    def mul(a, b):
        return a*b
        
    def div(a, b):
        # Safety check to prevent program crashes
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b
        
    a = float(input("Enter first number : "))
    b = float(input("Enter second number : "))
    print("Enter operation you want to perform : ")
    print("+, -, * or /")
    op = input().lower().strip()  

    if(op == "+"):
        output = add(a, b)
        print("Output: ", output)
    elif(op == "-"):
        output = sub(a, b)
        print("Output: ", output)
    elif(op == "*"):
        output = mul(a, b)
        print("Output: ", output)
    elif(op == "/"):
        output = div(a, b)
        print("Output: ", output)
    else:
        print("Invalid operation")

if __name__ == "__main__":
    calculate()
