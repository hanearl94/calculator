from unittest import result

print("============ Simple Calculator (+, -, *, /, %) ============")

while True:
    try:
        num1 = float(input("Enter the first number: "))

        op = input("Enter operation (+, -, *, /, %): ")

        num2 = float(input("Enter the second number: "))

        if op == "+":
            result == num1 + num2
        elif op == "-":
            result == num1 - num2
        elif op == "*":
            result == num1 * num2
        elif op == "/":
            if num2 != 0:
                result == num1 / num2
            else:
                result = "Error: Cannot divide by Zero"
        elif op == "%":
            if num2 != 0:
                result == num1 % num2
            else:
                result = "Error: Cannot modulo by Zero"
        else:
            result = "Error: Invalid operation."
    except ValueError:
        result = "Error: Invalid number."

    print("Result: ", result)
