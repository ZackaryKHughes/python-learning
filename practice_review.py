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