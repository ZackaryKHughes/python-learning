current_xp = int(input("Enter your current XP: "))
goal_xp = int(input("Enter your goal XP: "))
xp_needed = goal_xp - current_xp


if xp_needed <= 0:
    print("Congratulations! You have already reached your goal XP!")
else:
    while xp_needed > 0:
        print("You need", xp_needed, "XP to reach your goal.")
        xp_needed -= 1000
        print("Keep training! You are making progress.")

    print("Congratulations! You have reached your goal XP!")