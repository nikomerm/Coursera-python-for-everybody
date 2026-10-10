#Task_1 Write a function called double that takes one number and returns it multiplied by 2. Call the function with 8 and print the result.
# def double(x):
#     return x * 2

# print(double(8))

#Task_2 Write a function called full_name that takes a first name and a last name, and returns them joined with a space between. 
#Call it with your own names and store the result in a variable, then print that variable.

# def full_name(x,y):
#     return x + " " + y

# x="Nikos"
# y="Merm"
# result=full_name(x,y)
# print(result)

#Task_3 Write a function called show_total that takes a price and a quantity, and prints the total. 
#Call the function with 3.5 and 4. What does the call give back?

# def show_total(p,q):
#     print(p*q)

# show_total(3.5, 4)
# p=3.5
# q=4
# print(show_total(p,q))
#The answer to “What does the call give back?”: None.

#Task_4 Write a function called grade that takes a score and returns "Pass" if it is 50 or more, otherwise "Fail".
#Ask the user for a score, convert it, call the function with that value, and print the result.

# def grade(score):
#     if score >= 50:
#         return "Pass"
#     else:
#         return "Fail"

# u_score = input("Enter score: ")
# score_num = int(u_score)
# print(grade(score_num))

#Task_5 Write a function called bigger that takes two numbers and returns the larger one. 
# Ask the user for both numbers, call the function with them, and store the result in a variable called answer. Print answer.

def bigger(x, y):
    if x > y:
        return x
    else:
        return y

num_x = int(input("Enter number x: "))
num_y = int(input("Enter number y: "))
answer = bigger(num_x, num_y)
print(answer)