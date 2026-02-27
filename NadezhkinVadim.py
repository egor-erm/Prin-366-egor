days_of_week = [
    "ПОНЕДЕЛЬНИК",
    "ВТОРНИК",
    "СРЕДА",
    "ЧЕТВЕРГ",
    "ПЯТНИЦА",
    "СУББОТА",
    "ВОСКРЕСЕНЬЕ"
]

schedule = [
    # НЕДЕЛЯ 1
    [
        [
            {"time": "3-4", "subject": "ФИЗИЧЕСКАЯ КУЛЬУРА", "teacher": "Володина И.А.",
             "room": "УЛК 5"},
            {"time": "5-8", "subject": "РАСПРЕДЕЛИТЕЛЬНЫЙ КОНРОЛЬ ВЕРСИЙ КОДА", "teacher": "Сычев О.А.   Денисов",
             "room": "В 902-а"}
        ],
        [],
        [],
        [],
        [],
        [],
        []
    ],
    [
        [], [], [], [], [], [], []
    ]
]


def get_schedule(week, day):
    # Проверка корректности ввода
    if week not in [1, 2]:
        print("Ошибка: неделя должна быть 1 или 2")
        return

    if day not in range(1, 8):
        print("Ошибка: день должен быть от 1 до 7")
        return

    # Получаем расписание на этот день
    day_schedule = schedule[ week - 1][day - 1]

    # Вывод
    print("\n" + "=" * 60)
    print(f"РАСПИСАНИЕ ДЛЯ ГРУППЫ ПРИН-366")
    print(f"Неделя {week}, {days_of_week[day - 1]}")
    print("=" * 60)

    if not day_schedule:
        print("Отдыхаем")
    else:
        for lesson in day_schedule:
            print(f"\n {lesson['time']} пара")
            print(f"{lesson['subject']}")
            if lesson['teacher']:
                print(f" {lesson['teacher']}")
            if lesson['room']:
                print(f"{lesson['room']}")
            print("-" * 40)


while True:
    print("\n" + "=" * 60)
    print("Введите номер недели (1 или 2) и номер дня (1-7)")
    print("Или '0' для выхода")

    try:
        week = int(input("Неделя: "))
        if week == 0:
            print("Пока")
            break

        day = int(input("День (1-пн, 7-вс): "))

        get_schedule(week, day)

    except ValueError:
        print("Ошибка: введите числа!")