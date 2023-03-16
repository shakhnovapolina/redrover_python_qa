try:
    num1 = int(input("Введите число num1: "))
    num2 = int(input("Введите число num2: "))
    operator = input("Введите оператор: ")
    if operator == '/':
        result = num1 / num2
    elif operator:
        result = eval(f'{num1} {operator} {num2}')
        print(f'{num1} {operator} {num2} = {result}')
    else:
        print("Пустой оператор")
except ValueError:
    print("Введите не пустые значения")
except ZeroDivisionError:
    print("Деление на 0")
