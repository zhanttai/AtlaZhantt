from uuid import UUID

from core.models import Account


def save_account(account: Account):
    with open("./ATLA/Project/core/Account_List.txt", "a") as file:
        file.write(
            f"{account.owner_name}|{account.account_number}|{account.show_balance()}\n"
        )


def load_accounts():
    accounts: list[Account] = []
    try:
        with open("./Project/core/Account_List.txt", "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) != 3:
                    print(f"Ошибка строки: {line}")
                    continue

                name, number, balance = parts
                accounts.append(
                    Account(
                        name,
                        float(balance),
                        UUID(number),
                    )
                )

    except FileNotFoundError:
        print("Файл не найден, создается новый.")
        pass

    return accounts
