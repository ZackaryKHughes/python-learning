current_xp = int(input("Enter your current XP: "))
goal_xp = int(input("Enter your goal XP: "))
xp_needed = goal_xp - current_xp
xp_per_kill = int(input("Enter the XP you get per kill: "))


if xp_needed <= 0:
    print("Congratulations! You have already reached your goal XP!")
else:
    while xp_needed > 0:
        print("You need", xp_needed, "XP to reach your goal.")
        xp_needed -= xp_per_kill
        if xp_needed <= 0:
            break
        print("Keep training! You need " + str(xp_needed / xp_per_kill) + " kills to reach your goal.")

    print("Congratulations! You have reached your goal XP!")