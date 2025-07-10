#prompt the user to input their current age.
#the input() function gets user input as a string. int() is used to convert that string to an integer, as age is a number.

current_age = int(input("How old are you?"))

#calculate how old the user will be in the year 2050.Assume current year is 2023, so add 27 years to current age

years_to_add = 2050 - 2023
future_age = current_age + years_to_add

#print the user's age in 2050 in the specified format
#using an f-string for easy variable embedding.

print(f"In 2050, you will be {future_age} years old.")
