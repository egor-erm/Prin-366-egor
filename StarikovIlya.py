# Конвертер валют в рубли

print("Конвертер валют")

USD = 76.73
EUR = 90.35
CNY = 11.11
JPY = 0.49

while True:
    try:
        rubles = float(input("\nВведите сумму в рублях: "))

        print("Список валют:\n" "1: USD\n" "2: EUR\n" "3: CNY\n" "4: JPY\n")

        currency = int(input("Введите необходимую вам валюту: "))

        if(currency == 1):
            print(f"{rubles} рублей = {rubles/USD} долларов")
        elif(currency == 2):
            print(f"{rubles} рублей = {rubles/EUR} евро")
        elif(currency == 3):
            print(f"{rubles} рублей = {rubles/CNY} юань")
        elif(currency == 4):
            print(f"{rubles} рублей = {rubles/JPY} йен")
        else:
            print("Ошибка!!! Такой валюты нет!")
            
    except ValueError:
        print("Ошибка. Нужно вводить числа")