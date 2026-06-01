# Monthly Income
monthly_income = float(input("Enter your monthly income: "))
side_hustle_income = float(input("Enter your monthly side hustle income (if any, otherwise enter 0): "))
total_monthly_income = monthly_income + side_hustle_income
month = 1



# Monthly Expenses
fixed_expenses = float(input("Enter your monthly rent/mortgage: ")) + float(input("Enter your monthly utilities: ")) + float(input("Enter your monthly car payment: ")) + float(input("Enter your monthly insurance: ")) + float(input("Enter your monthly entertainment expenses: ")) + float(input("Enter your monthly phone bill: ")) + float(input("Enter your monthly internet bill: ")) + float(input("Enter your monthly debt payments (if any, otherwise enter 0): "))
extra_spending = float(input("Enter your monthly groceries: ")) + float(input("Did you eat out this month? How much was it total?: ")) + float(input("Enter your monthly gas expenses: "))
total_monthly_expenses = fixed_expenses + extra_spending
leftover_money = total_monthly_income - total_monthly_expenses



# Summary of expenses and income
if total_monthly_income > total_monthly_expenses and extra_spending > 0:
    print("Your total monthly income is $" + str(total_monthly_income) + " and your total monthly expenses are $" + str(total_monthly_expenses) + ". You are on track to reach your savings goal!")
else:
    while total_monthly_income <= total_monthly_expenses:
       print("Lets find out where we can cut back on expenses. Your total monthly income is $" + str(total_monthly_income) + " and your total monthly expenses are $" + str(total_monthly_expenses) + ".")
       print("Your fixed expenses are $" + str(fixed_expenses) + " and your extra spending is $" + str(extra_spending) + ".")
       print("Try to cut back on your extra spending to save more money each month.")
       extra_spending -= float(input("Enter how much you can cut back on your extra spending: "))
       print("Great! Your new total monthly expenses are $" + str(fixed_expenses + extra_spending) + ".")
       total_monthly_expenses = fixed_expenses + extra_spending
       leftover_money = total_monthly_income - total_monthly_expenses
     

# Savings Goal Calculator
current_savings = float(input("Enter your current savings: "))
savings_goal = float(input("Enter your savings goal: "))
money_needed = savings_goal - current_savings


# Goal Calculation per month
if money_needed <= 0:
    print("Congratulations! You have already reached your savings goal!")
else:
    while money_needed > 0:
        print("Month", month)
        print("You need $" + str(money_needed) + " to reach your savings goal.")

        payment_this_month = float(input("Enter how much of " + str(leftover_money) + " you saved this month: "))
        money_needed -= payment_this_month
        leftover_money -= payment_this_month
        leftover_money += total_monthly_income - total_monthly_expenses

        if money_needed > 0:
            print("Keep saving! You need $" + str(money_needed) + " more to reach your goal.")
        else:
            print("Congratulations! You have reached your savings goal!")
        month += 1

