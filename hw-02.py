result = None
operand = None
operator = None
wait_for_number = True  # це флаг який нам допоможе перемикати логічні гілки
while True:
    user_input = input("Enter : ")  # введемо нову змінну
    if user_input == "=":  # якщо прийде знак = то виводимо результат та зупиняємо цикл
        print(result)
        break
    if (
        wait_for_number
    ):  # ця логічна гілка працює коли флаг wait_for_number в положенні True
        try:  # перевірка на число
            operand = float(user_input)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            continue
        wait_for_number = False  # якщо перший operand отримали - переключаємо флаг в False і цикл починається спочатку
        if (
            not result
        ):  # тут зрозуміло що на першій ітерації результата ще немає, тому присваюваємо в резалт наш перший operand
            result = operand
        if operator == "+":
            result = float(result + operand)
        elif operator == "-":
            result = float(result - operand)
        elif operator == "*":
            result = float(result * operand)
        elif operator == "/":
            try:
                result = float(result / operand)
            except ZeroDivisionError:
                print("You can never divide by Zero!")
                continue
    else:  # ця логічна гілка працює коли флаг wait_for_number в положенні False
        if user_input in ["+", "-", "*", "/"]:
            operator = user_input
            wait_for_number = True
        else:
            print("Помилка: неправильний оператор")
