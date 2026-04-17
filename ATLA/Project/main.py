from core.models import Account, CreditPlans, PremiumAccount
from core.storage import load_accounts, save_account


def main():
    # Загрузка всех аккаунтов
    print(load_accounts())

    # Создание обычного аккаунта
    my_account = Account("Ulugbek", 0)
    my_account.deposit(10000)
    my_account.withdraw(500)
    save_account(my_account)

    print(my_account.show_balance())
    print(my_account.account_number)

    # Создание премиум аккаунта
    acc2 = PremiumAccount("Ne_Zhantai", 1000)
    acc2.deposit(500)
    print("Balance acc2:", acc2.show_balance())
    save_account(acc2)

    # Кредитное предложение
    credit = CreditPlans()
    plan = credit.generate_plan(10000)

    print("Кредитное предложение:")
    print(f"Сумма: {plan['amount']}")
    print(f"Срок: {plan['term']} месяцев")
    print(f"Процент: {plan['percent']}%")
    print(f"Ежемесячный платеж: {plan['monthly_payment']}")
    print(f"Итого к выплате: {plan['total']}")


if __name__ == "__main__":
    main()


