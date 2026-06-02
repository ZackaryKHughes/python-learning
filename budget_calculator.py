from budget_functions import normalize_month
from budget_functions import get_records
from budget_functions import calculate_total
from budget_functions import calculate_checking_balance
from budget_functions import transfer_money
from budget_functions import calculate_goal_progress
from budget_functions import save_balances
from budget_functions import load_balances

reset = input("Reset balances? (y/n): ")

if reset.lower() == "y":
    checking_balance = 0
    savings_balance = 0
    emergency_balance = 0
    investment_balance = 0

    save_balances(
        checking_balance,
        savings_balance,
        emergency_balance,
        investment_balance
    )

else:
    checking_balance, savings_balance, emergency_balance, investment_balance = load_balances()


month = normalize_month(input("Enter budget month: "))

while month == "Invalid Month":
    print("Invalid month. Try again.")
    month = normalize_month(input("Enter budget month: "))

year = int(input("Enter budget year: "))


checking_balance, savings_balance, emergency_balance, investment_balance = load_balances()


print("----- Starting Balances -----")
print("Checking: $" + str(checking_balance))
print("Savings: $" + str(savings_balance))
print("Emergency Fund: $" + str(emergency_balance))
print("Investments: $" + str(investment_balance))


print("----- Income for " + month + " " + str(year) + " -----")
income_records = get_records("income", month, year)
total_income = calculate_total(income_records)


print("----- Expenses for " + month + " " + str(year) + " -----")
expense_records = get_records("expense", month, year)
total_expenses = calculate_total(expense_records)


checking_balance = calculate_checking_balance(
    checking_balance,
    total_income,
    total_expenses
)


print("----- Monthly Summary -----")
print("Month: " + month + " " + str(year))
print("Total Income: $" + str(total_income))
print("Total Expenses: $" + str(total_expenses))
print("Checking After Income and Expenses: $" + str(checking_balance))


savings_goal = float(input("Enter your savings goal: "))
emergency_goal = float(input("Enter your emergency fund goal: "))
investment_goal = float(input("Enter your investment goal: "))


savings_transfer = float(input("How much do you want to move to savings? "))
checking_balance, savings_balance = transfer_money(
    checking_balance,
    savings_balance,
    savings_transfer
)


emergency_transfer = float(input("How much do you want to move to emergency fund? "))
checking_balance, emergency_balance = transfer_money(
    checking_balance,
    emergency_balance,
    emergency_transfer
)


investment_transfer = float(input("How much do you want to move to investments? "))
checking_balance, investment_balance = transfer_money(
    checking_balance,
    investment_balance,
    investment_transfer
)


savings_needed = calculate_goal_progress(savings_goal, savings_balance)
emergency_needed = calculate_goal_progress(emergency_goal, emergency_balance)
investment_needed = calculate_goal_progress(investment_goal, investment_balance)


print("----- Income Records -----")
for income in income_records:
    print(income["month"], income["year"])
    print(income["name"] + ": $" + str(income["amount"]))


print("----- Expense Records -----")
for expense in expense_records:
    print(expense["month"], expense["year"])
    print(expense["name"] + ": $" + str(expense["amount"]))


print("----- Ending Balances -----")
print("Checking: $" + str(checking_balance))
print("Savings: $" + str(savings_balance))
print("Emergency Fund: $" + str(emergency_balance))
print("Investments: $" + str(investment_balance))


print("----- Goal Progress -----")

if savings_needed <= 0:
    print("Savings goal reached!")
else:
    print("Savings needed: $" + str(savings_needed))

if emergency_needed <= 0:
    print("Emergency fund goal reached!")
else:
    print("Emergency fund needed: $" + str(emergency_needed))

if investment_needed <= 0:
    print("Investment goal reached!")
else:
    print("Investment needed: $" + str(investment_needed))


save_balances(
    checking_balance,
    savings_balance,
    emergency_balance,
    investment_balance
)

print("Balances saved for next month.")