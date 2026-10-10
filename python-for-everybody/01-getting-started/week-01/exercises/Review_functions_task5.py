#Task 5: Different names for arguments
#Write is_adult(age) that returns True if age >= 18, otherwise False.
#  Ask the user for their age with input(), convert it, and store it in a variable named user_age.
#  Call the function with user_age and print the result. 
# Is age the same variable as user_age? 
# Where does each one exist?


#task5
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

u_age = input("Enter your age: ")
user_age = int(u_age)
print(is_adult(user_age))

#age is the parameter, which exists only inside the function.
#user_age is the argument, which exists outside the function.
#They are two different variables. The call copies the value of user_age into age.
#print(age) after the function gives NameError.

#Parameter: the name in the definition (age).
#Argument: the value you pass in the call (user_age).
#Call: running the function by writing its name with parentheses.
#Return: sends a value back to the call so you can store, print, or use it