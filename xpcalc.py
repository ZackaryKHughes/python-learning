current_xp = int(input("Enter your current XP: "))
goal_xp = int(input("Enter your goal XP: "))
xp_needed = goal_xp - current_xp
per_black_demon = int(input("Enter the XP you get per Black Demon kill: "))


if xp_needed <= 0:
    print("Congratulations! You have already reached your goal XP!")
else:
    while xp_needed > 0:
        print("You need", xp_needed, "XP to reach your goal.")
        xp_needed -= int(per_black_demon)
        print("Keep training! You need " + str(xp_needed / per_black_demon) + " kills to reach your goal.")

    print("Congratulations! You have reached your goal XP!")