current_savings = float(input("Enter your current savings: "))
savings_goal = float(input("Enter your savings goal: "))
weekly_savings_goal = float(input("Enter how much you can save each week: "))
monthly_savings_goal = weekly_savings_goal * 4
money_needed = savings_goal - current_savings
payment_this_month = float(input("Enter how much you saved this month: "))

# Goal Calculation per month
if current_savings >= savings_goal:
    print("Congratulations! You have already reached your savings goal!")
else:
    while money_needed > 0:
        print("You need $" + str(money_needed) + " to reach your savings goal.")
        money_needed -= monthly_savings_goal
        if money_needed <= 0:
            break
        print("Keep saving! You need " + str(money_needed / monthly_savings_goal) + " months to reach your goal.")

    if payment_this_month >= monthly_savings_goal:
        print("Great job! You have saved enough this month to stay on track for your goal.")
    else:
        print("You need to save more this month to stay on track for your goal. You need $" + str(monthly_savings_goal - payment_this_month) + " more this month.")

print("Congratulations! You have reached your savings goal!")

