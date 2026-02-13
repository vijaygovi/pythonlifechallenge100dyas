#list comphiresion 
list=["Even" if i%2==0 else "odd" for i in range(10)]
print(list)

fruits=["APPLE","BANANA","ORANGE","MANGO"]
NEWLIST=[x for x in fruits if "P" in x]
print(NEWLIST)

s=[1,2,3,4,5,6,7,8,9]
for i in range(len(s)):
    print(s[i])
    
    str=[1,2,3,4,5,6,7,8,9,9,8,6,7,6,7,7,7,7,7,5,4,3,3]
    n=[]
    
    for i in str:
        if i not in n:
            n.append(i)
            print(n)


# A simple program to greet the user and estimate a future year

# Ask the user for their name and store it in a variable
user_name = input("Hello! What is your name? ")

# Ask the user for their age and convert the input string to an integer
user_age = int(input(f"Nice to meet you, {user_name}! How old are you? "))

# Calculate the year the user will turn 100
# We assume the current year is 2025 based on the context data provided.
current_year = 2025
year_hundred = current_year + (100 - user_age)

# Print a greeting and the calculated year
print(f"\n{user_name}, you will turn 100 years old in the year {year_hundred}!")


# A program to check if a number is even or odd

# Get a number input from the user and convert it to an integer
number = int(input("Enter a number to check if it's even or odd: "))

# Check the remainder when the number is divided by 2
if number % 2 == 0:
    print(f"The number {number} is Even.")
else:
    print(f"The number {number} is Odd.")

