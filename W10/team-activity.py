bank_accounts = []
account_balances = []

while True:
    account_name = input("What is the name of this account? ")

    if account_name == "quit":
        break

    account_balance = float(input("What is the balance? "))
    bank_accounts.append(account_name)
    account_balances.append(account_balance)

print("Account Information:")
print()

total = 0

for i in range(len(bank_accounts)):
    total += account_balances[i]
    print(f"{bank_accounts[i]} - ${account_balances[i]:.2f}")


print()

print(f"Total: ${total:.2f}")
print(f"Average: ${(total / len(bank_accounts)):.2f}")
