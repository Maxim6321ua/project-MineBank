server_economy = {
    'Admin': 999999,
    'Steve': 0,
    'Alex': 150
}

print("---  MineBank Console v1.0  ---")
print("Доступні команди:")
print("  !reg [нік]              - Зареєструвати нового гравця (+100 монет)")
print("  !balance [нік]          - Перевірити баланс гравця")
print("  !give [нік] [сума]      - (Admin) Видати гроші гравцю")
print("  !pay [хто] [кому] [сума]- Переказ грошей між гравцями")
print("  !top                    - Показати всіх гравців")
print("  !exit                   - Вийти з консолі")
print("--------------------------------------")

while True:
    user_input = input("\nВведіть команду: ").strip()


    parts = user_input.split()

    if len(parts) == 0:
        continue

    command = parts[0].lower()

    if command == '!reg':
        if len(parts) > 1:
            nickname = parts[1]

            if nickname in server_economy:
                print(f" Помилка: Гравець {nickname} вже існує!")
            else:
                server_economy[nickname] = 100
                print(f" Успіх: Гравець {nickname} зареєстрований! Баланс: 100")
        else:
            print(" Використання: !reg [нікнейм]")

    elif command == '!balance' or command == '!bal':
        if len(parts) > 1:
            nickname = parts[1]
            if nickname in server_economy:
                balance = server_economy[nickname]
                print(f" Баланс гравця {nickname}: {balance} монет")
            else:
                print(f" Помилка: Гравця {nickname} не знайдено.")
        else:
            print("Використання: !balance [нікнейм]")

    elif command == '!give':
        if len(parts) > 2:
            nickname = parts[1]
            amount_str = parts[2]

            if amount_str.isdigit():
                amount = int(amount_str)

                if nickname in server_economy:
                    server_economy[nickname] += amount
                    print(f"Адмін видав {amount} монет гравцю {nickname}.")
                else:
                    print(f" Гравець {nickname} не знайдений.")
            else:
                print("Сума має бути числом!")
        else:
            print(" Використання: !give [нік] [сума]")

    elif command == '!pay':
        if len(parts) > 3:
            sender = parts[1]
            receiver = parts[2]
            amount_str = parts[3]

            if amount_str.isdigit():

                amount = int(amount_str)

                if sender in server_economy and receiver in server_economy:
                    if server_economy[sender] >= amount:
                        server_economy[sender] -= amount
                        server_economy[receiver] += amount
                        print(f" {sender} переказав {amount} монет гравцю {receiver}.")
                        print(f"Новий баланс {sender}: {server_economy[sender]}")
                        print(f"Новий баланс {receiver}: {server_economy[receiver]}")
                    else:
                        print(f" У {sender} недостатньо грошей!")
                else:
                    print(" Обидва гравці повинні бути зареєстровані!")
            else:
                print("Сума має бути числом!")
        else:
            print("Використання: !pay [від_кого] [кому] [сума]")

    elif command == '!top':
        print("\n=== СПИСОК ГРАВЦІВ ===")
        for name, money in server_economy.items():
            print(f"- {name}: {money} $")
        print("=========================")

    elif command == '!exit':
        print("Роботу завершено. До побачення!")
        break
    else:
        print(f"Невідома команда: {command}")