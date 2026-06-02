slayer_lvl = int(input("What is your current Slayer level? "))

if slayer_lvl >= 50:
    print("You have already unlocked Bloodvelds.")
else:
    while slayer_lvl < 50:
        print("Your current Slayer level " + str(slayer_lvl) + " is too low. ")
        slayer_lvl += 1

    print("Bloodvelds unlocked!")