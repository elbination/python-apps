while True:
    try:
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
    except ValueError:
        print("Please check your input!")
        continue
    cal = ""
    print("""
    Options:
    Enter '+' to add two numbers
    Enter '-' to subtract two numbers
    Enter '*' to multiply two numbers
    Enter '/' to divide two numbers
    Enter 'quit' to end the program
    """)
    operation = input("Operation: ")
    if operation == "quit":
        break
    elif operation == "+":
        cal = x + y
    elif operation == "-":
        cal = x - y
    elif operation == "/":
        if y == 0:
            print("Second number must != 0. \nPlease try again :)")
            continue
        else:
            cal = float(x/y)
    elif operation == "*":
        cal = x * y
    else:
        print("Unknown input \nPlease check your input")
        continue
    print("Result: ", x, operation, y, " = ", cal)
    ask = input("Do you want to continue the program? (y/n): ")
    if ask == "y":
        continue
    elif ask == "n":
        break
    else:
        print("Unknown input! \nProgram will continue")
        continue



