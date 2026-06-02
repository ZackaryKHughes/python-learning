def normalize_month(month):
    month = month.lower().strip()

    month_map = {
        "jan": "January",
        "january": "January",
        "feb": "February",
        "february": "February",
        "mar": "March",
        "march": "March",
        "apr": "April",
        "april": "April",
        "may": "May",
        "jun": "June",
        "june": "June",
        "jul": "July",
        "july": "July",
        "aug": "August",
        "august": "August",
        "sep": "September",
        "sept": "September",
        "september": "September",
        "oct": "October",
        "october": "October",
        "nov": "November",
        "november": "November",
        "dec": "December",
        "december": "December"
    }

    return month_map.get(month, "Invalid Month")


def get_records(record_type, month, year):
    records = []

    while True:
        name = input(f"Enter {record_type} name or type done: ")

        if name.lower() == "done":
            break

        amount = float(input(f"Enter {record_type} amount: "))

        record = {
            "name": name,
            "amount": amount,
            "month": month,
            "year": year
        }

        records.append(record)

    return records


def calculate_total(records):
    total = 0

    for record in records:
        total += record["amount"]

    return total


def calculate_checking_balance(starting_checking, income, expenses):
    return starting_checking + income - expenses


def transfer_money(checking_balance, account_balance, amount):
    checking_balance -= amount
    account_balance += amount

    return checking_balance, account_balance


def calculate_goal_progress(goal, current_balance):
    return goal - current_balance


def save_balances(checking, savings, emergency, investments):
    file = open("balances.txt", "w")

    file.write(str(checking) + "\n")
    file.write(str(savings) + "\n")
    file.write(str(emergency) + "\n")
    file.write(str(investments) + "\n")

    file.close()


def load_balances():
    try:
        file = open("balances.txt", "r")

        checking = float(file.readline())
        savings = float(file.readline())
        emergency = float(file.readline())
        investments = float(file.readline())

        file.close()

        return checking, savings, emergency, investments

    except FileNotFoundError:
        print("No saved balances found. Enter starting balances.")

        checking = float(input("Enter checking balance: "))
        savings = float(input("Enter savings balance: "))
        emergency = float(input("Enter emergency fund balance: "))
        investments = float(input("Enter investment balance: "))

        return checking, savings, emergency, investments