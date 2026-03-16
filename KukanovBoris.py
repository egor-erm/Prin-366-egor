firstNumber = int(input("Введите первое число: "))

secondNumber = int(input("Введите второе число: "))

operation = int(input("Введите номер операции:\n"
                      "1. +\n"
                      "2. -\n"
                      "3. *\n"
                      "4. /\n"
                      "Операция: "))

match operation: # Свич для выбранной операции
    case 1:
        result = firstNumber + secondNumber
    case 2:
        result = firstNumber - secondNumber
    case 3:
        result = firstNumber * secondNumber
    case 4:
        if (secondNumber == 0):
            print("НЕЛЬЗЯ ДЕЛИТЬ НА НОЛЬ!!!!!!") # Точно нельзя
            result = "Ошибка!"
        else:
            result = firstNumber / secondNumber
    case _:
        print("Операция не выбрана")
        result = "Ошибка!"

print(f"Результат операции: {result}")