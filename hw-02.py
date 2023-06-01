result = None
operand = None
operator = None
wait_for_number = True

while True:
    wait_for_number = int(input("Enter : "))
    operator = input('"+", "-", "*", "/" :')

    # operand = int(input(''))
    # if wait_for_number in ('"+", "-", "*", "/"'):
    try:
        operand = int(input("enter a number: "))

        if operator == "+":
            result = float(operand + operand)
        elif operator == "-":
            result = float(operand - operand)
        elif operator == "*":
            result = float(operand * operand)
        elif operator == "/":
            result = float(operand / operand)
        elif wait_for_number == "=":
            print(result)
            break

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        continue
    except ZeroDivisionError:
        print("You can never divide by Zero!")
        continue
    except SyntaxError:
        print("SyntaxError: Please Use Numbers Only")

print(result)
