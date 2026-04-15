def save_accounts(accounts_list):
    with open("./Project/core/Account_List.txt", "w") as file:
        for acc in accounts_list:
            file.write(f"{acc.owner_name}|{acc.account_number}|{acc.show_balance()}\n")


def load_accounts():
    accounts = []

    try: #Try, except
        with open("./Project/core/Account_List.txt", "r") as file:
            from core.models import Account
            for line in file:
                parts = [p.strip() for p in line.strip().split("|")]
                if len(parts) != 3: #GPT
                    print(f"Ошибка строки: {line}") #GPT
                    continue #GPT
                name, number, balance = parts
                acc = Account(name, float(balance))
                acc.account_number = int(number)
                accounts.append(acc)
    except FileNotFoundError:
        pass
    return accounts