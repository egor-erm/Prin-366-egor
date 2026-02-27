# Простой менеджер задач (To-Do List)
# Основа для будущих доработок

tasks = []  # Список для хранения задач

def show_tasks():
    """Показывает все задачи."""
    if not tasks:
        print("Список задач пуст.")
    else:
        print("\nВаши задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    """Добавляет новую задачу."""
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print(f"Задача '{task}' добавлена!")

def delete_task():
    """Удаляет задачу по номеру."""
    show_tasks()
    try:
        num = int(input("Введите номер задачи для удаления: "))
        removed = tasks.pop(num - 1)
        print(f"Задача '{removed}' удалена.")
    except (IndexError, ValueError):
        print("Ошибка: неверный номер.")

# Основной цикл программы
while True:
    print("\n--- Меню ---")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выход")
    
    choice = input("Выберите действие: ")
    
    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("До свидания!")
        break
    else:
        print("Неверный ввод, попробуйте снова.")