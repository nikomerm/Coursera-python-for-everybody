#Task 4: Print versus return
#Write two functions, add_print(a, b) that only prints the sum, and add_return(a, b) that returns it. 
# Try x = add_print(2, 3) and y = add_return(2, 3), then print x and y. 
# What is in each variable, and why?


#task4
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return (a + b)

x= add_print(2,3)
y= add_return(2,3)
print(x)
print(y)

#print shows a value on the screen. The value is not kept, so nothing is left for your code to use.
#return hands a value back to the call, so you can store it (y = add_return(2, 3)), print it, or use it in a decision.