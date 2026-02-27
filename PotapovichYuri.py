import random
import string

def generate_password(length):
    """Генерирует случайный пароль заданной длины."""
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Генератор паролей")
    while True:
        try:
            length = int(input("Введите длину пароля (или 0 для выхода): "))
            if length == 0:
                print("Выход из программы.")
                break
            if length < 4:
                print("Рекомендуется длина не менее 4 символов.")
            password = generate_password(length)
            print(f"Сгенерированный пароль: {password}\n")
        except ValueError:
            print("Ошибка: введите целое число.\n")

if __name__ == "__main__":
    main()