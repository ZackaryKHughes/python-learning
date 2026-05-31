range_level = int(input("What is your range level? "))

if range_level >= 90:
    print("You can use a Dragon Hunter Crossbow. You are crushing it!")
elif range_level >= 75:
    print("You can use a Toxic Blowpipe. You are doing great!")
elif range_level >= 61:
    print("You can use a Rune Crossbow. You are okay I guess.")
else:
    print("You need to step it up if you want to be a good ranger. You can only use a Maple Shortbow.")

print("Range is my favorite skill to train.")
