# Functions Basic 

def sumFunc():
    a = 4
    b = 8
    sum = a + b
    print(sum)


sumFunc()   # print  12
# Function Calling

# # .... 100 line of code 

sumFunc()   # print 12

# # .... 100 line of code 

sumFunc()   # print 12

# Wrtie a function named welcome_message() that prints "Welcone to Python Programming! " three times

# Simple Function Definition without Parameters
def welcome_message():
    print("Welcome to Python Programming!")
    print("Line2")
welcome_message()   # Function is being called
welcome_message()   # Function is being called
welcome_message()   # Function is being called

# Define a function inspire() that prints a motivational quote with your name.

# Function Definition

def inspire():
    print("You are the master of your destiny: Mishirjii")
inspire()

# # Simple Function Call with No Argument
def IamBest():
    print("Just a Trial Function")
IamBest()

# # Paramenter in Functions

# # Function Definition with Parameter
def average(a = 10, b = 10):
    avergaeValue = (a + b) / 2
    print(avergaeValue)

# # Function Calling with Arguments 
average(5, 10)
average(7, 10)
average(80, 98)
average()

# # Write a function show_age(name, age) that prints: "Mishirji is 19 year old."

def show_age(name = "Mishirji", age = 19):
    print(f"{name} is {age} years old")
show_age("Mishirji", 19)
show_age()
show_age("Fuddi", 69)

# # Return Statement 

def multiply(a = 10, b = 10):
    return a * b
print(multiply(10, 10))
result = multiply(5, 10)
print(result)

# # Write a function square(num) that returns the square of a number.

def square(num = 10):
    return num ** 2
print(square())
print(square(2))

# # Write a function that takes a string and return the count of vowels and consonants seperately

def countVowConso(userInput):
    # define vowels
    vowels = "aeiouAEIOU"

    countVowel = 0
    countConsonants = 0

    for eachChar in userInput:
        if (eachChar.isalpha()):
            if(eachChar in vowels):
                countVowel += 1
            else:
                countConsonants += 1
    return countVowel, countConsonants

# # Function Call

vowels, consonants = countVowConso("Mishirjii")

print(vowels, consonants)

