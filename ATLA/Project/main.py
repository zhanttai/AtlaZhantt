from core.storage import save_accounts, load_accounts
from core.models import Account, CreditPlans


def main():
    accounts = load_accounts()

    my_account = Account("Zhantai", 0)
    my_account.deposit(1000)

    accounts.append(my_account)

    credit = CreditPlans()
    plan = credit.generate_plan(10000)

    print("Кредитное предложение:")
    print(f"Сумма: {plan['amount']}")
    print(f"Срок: {plan['term']} месяцев")
    print(f"Процент: {plan['percent']}%")
    print(f"Ежемесячный платеж: {plan['monthly_payment']}")
    print(f"Итого к выплате: {plan['total']}")

    save_accounts(accounts)


if __name__ == "__main__":
    main()