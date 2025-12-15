import random

server_economy = {
    'Admin': 999999,
    'Steve': 0,
    'Alex': 150
}

gift_text = {
    "money_loser": "You got very little money, maybe Santa bought RAM for his PC.",
    "money_winner": "Wow! You are very lucky, you got a lot of money! Maybe Santa is rich."
}

print("--- MineBank Console v1.0 ---")
print("Available commands:")
print("  !reg [nick]              - Register a new player (+100 coins)")
print("  !balance [nick]          - Check player balance")
print("  !give [nick] [amount]    - (Admin) Give money to player")
print("  !pay [sender] [to] [amt] - Transfer money between players")
print("  !top                     - Show all players")
print("  !gift [nick]             - Get a random gift (100-1000 coins)")
print("  !exit                    - Exit console")
print("--------------------------------------")

while True:
    user_input = input("\nEnter command: ").strip()

    parts = user_input.split()

    if len(parts) == 0:
        continue

    command = parts[0].lower()

    if command == '!reg':
        if len(parts) > 1:
            nickname = parts[1]

            if nickname in server_economy:
                print(f" Error: Player {nickname} already exists!")
            else:
                server_economy[nickname] = 100
                print(f" Success: Player {nickname} registered! Balance: 100")
        else:
            print(" Usage: !reg [nickname]")

    elif command == '!balance' or command == '!bal':
        if len(parts) > 1:
            nickname = parts[1]
            if nickname in server_economy:
                balance = server_economy[nickname]
                print(f" Player {nickname} balance: {balance} coins")
            else:
                print(f" Error: Player {nickname} not found.")
        else:
            print("Usage: !balance [nickname]")

    elif command == '!give':
        if len(parts) > 2:
            nickname = parts[1]
            amount_str = parts[2]

            if amount_str.isdigit():
                amount = int(amount_str)

                if nickname in server_economy:
                    server_economy[nickname] += amount
                    print(f"Admin gave {amount} coins to {nickname}.")
                else:
                    print(f" Player {nickname} not found.")
            else:
                print("Amount must be a number!")
        else:
            print(" Usage: !give [nick] [amount]")

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
                        print(f" {sender} transferred {amount} coins to {receiver}.")
                        print(f"New balance {sender}: {server_economy[sender]}")
                        print(f"New balance {receiver}: {server_economy[receiver]}")
                    else:
                        print(f" {sender} does not have enough money!")
                else:
                    print(" Both players must be registered!")
            else:
                print("Amount must be a number!")
        else:
            print("Usage: !pay [sender] [receiver] [amount]")

    elif command == '!top':
        print("\n=== PLAYER LIST ===")
        for name, money in server_economy.items():
            print(f"- {name}: {money} $")
        print("======================")

    elif command == '!gift':
        if len(parts) > 1:
            nickname = parts[1]
            if nickname in server_economy:
                gift_amount = random.randint(100, 1000)
                server_economy[nickname] += gift_amount
                
                if gift_amount < 500:
                    print(gift_text["money_loser"])
                else:
                    print(gift_text["money_winner"])
                
                print(f"Player {nickname} received a gift: {gift_amount} coins! New balance: {server_economy[nickname]}")
            else:
                print(f"Error: Player {nickname} not found.")
        else:
            print("Usage: !gift [nickname]")

    elif command == '!exit':
        print("Shutting down. Goodbye!")
        break
    else:
        print(f"Unknown command: {command}")