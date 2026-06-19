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
    print("add, sub, mul or div")
    op = input().lower().strip()  

    if(op == "add"):
        output = add(a, b)
        print("Output: ", output)
    elif(op == "sub"):
        output = sub(a, b)
        print("Output: ", output)
    elif(op == "mul"):
        output = mul(a, b)
        print("Output: ", output)
    elif(op == "div"):
        output = div(a, b)
        print("Output: ", output)
    else:
        print("Invalid operation")

if __name__ == "__main__":
    calculate()
