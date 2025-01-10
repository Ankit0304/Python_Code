
while True:
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print(''' Select Operation: 
1.Addition
2.Subtraction
3.Multiplication
4.Division''')

    print("Enter 1, 2, 3, or 4 to perform the operation")
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        result = num1 + num2
        operation = "+"
    elif choice == '2':
        result = num1 - num2
        operation = "-"
    elif choice == '3':
        result = num1 * num2
        operation = "*"
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
            operation = "/"
    else:
        result = "Invalid Input"
        operation = ""

    if operation:
        print(num1, operation, num2, "=", result)
    else:
        print(result)
        
     next_calculation = input("Do you want to perform another calculation? (y/n): ")
    if next_calculation.lower() != "y":
        break
