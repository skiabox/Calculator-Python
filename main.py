def calculate(a, b, operator):
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        case _:
            return "Invalid operator"

while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        o = input("Operator (+, -, *, /) or q to quit: ")

        if o == "q":
            break

        result = calculate(a, b, o)
        print(f"Result: {result}")

    except ValueError as e:
        print(e)

    except ZeroDivisionError as e:
        print(e)