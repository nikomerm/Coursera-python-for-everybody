#Task 3: Two parameters, order matters
#Write subtract(a, b) that returns a - b. 
# Call subtract(10, 3) and then subtract(3, 10). 
# Why are the results different? 
# Which are the parameters and which are the arguments?


#task3
def substract(a, b):
    return a - b

print(substract(10, 3)) # 7  
print(substract(3, 10)) # -7

#The results differ because arguments go to parameters by position: the first argument goes to a, the second to b.
