current_savings = float(input("Enter your current savings: "))
savings_goal = float(input("Enter your savings goal: "))
money_needed = savings_goal - current_savings
month = 1

# Goal Calculation per month
if money_needed <= 0:
    print("Congratulations! You have already reached your savings goal!")
else:
    while money_needed > 0:
        print("Month", month)
        print("You need $" + str(money_needed) + " to reach your savings goal.")

        payment_this_month = float(input("Enter how much you saved this month: "))
        money_needed -= payment_this_month

        if money_needed > 0:
            print("Keep saving! You need $" + str(money_needed) + " more to reach your goal.")
        else:
            print("Congratulations! You have reached your savings goal!")
        month += 1
