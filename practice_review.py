#============================
# Python Practice Review
#============================

print("Welcome to Python practice review!")
print("----------------------------------")

# Variables and Data Types

name= "Zackary"
age = 31
weight = 220.2
is_learning = True

print(name)
print(age)
print(weight)
print(is_learning)

# What type is name? String (Text)
print(type(name))
# What type is age? Integer (whole number)
print(type(age))
# What type is weight? Float (decimal number))
print(type(weight))
# What type is is_learning? Boolean (True or False)
print(type(is_learning))
# What will print to the screen? "Zackary is 31 years old, weighs 220.2 pounds, and is learning Python: True"
print(f"{name} is {age} years old, weighs {weight} pounds, and is learning Python: {is_learning}")


# =========================
# 2. User Input
# =========================

user_name = input("What is your name? ")

print("Hello", user_name)

# What type is user_name? String (Text)
# What value is stored in user_name? The name the user inputs when prompted
# What will print? Hello then the user inputs for their name. 

# =========================
# 3. Integers and Math
# =========================

current_xp = int(input("Enter your current XP: "))
goal_xp = int(input("Enter your goal XP: "))

xp_needed = goal_xp - current_xp

print("You need " + str(xp_needed) + " XP to reach your goal.")

# Current XP: 75000
# Goal XP: 100000
# What type is current_xp? Integer (whole number)
# What type is goal_xp? Integer (whole number)
# What value gets stored in xp_needed? The difference between goal_xp and current_xp, which is the amount of XP needed to reach the goal. In this case, xp_needed would be 25000 (100000 - 75000).
# What will print? "You need then the value of xp_needed then XP to reach your" goal. In this case, it would print "You need 25000 XP to reach your goal."

# =========================
# 4. If / Else
# =========================

if xp_needed <= 0:
    print("You already reached your goal!")
else:
    print("Keep training!")

    # What is xp_needed? The amount of XP needed to reach the goal, calculated as the difference between goal_xp and current_xp.
    # Is xp_needed <= 0 True or False? False, because xp_needed is 25000, which is greater than 0.
    # Which block runs? The else block runs because the condition in the if statement is False. It will print "Keep training!" to the screen.
    # What prints? "Keep training!" because the condition in the if statement is False, so the else block executes.