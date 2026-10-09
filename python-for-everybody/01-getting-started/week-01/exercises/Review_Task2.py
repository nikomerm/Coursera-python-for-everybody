#Task 2: Precedence
#Without running anything, predict the result of 2 + 3 * 4 ** 2 - 10 / 5. Then run it and compare. If you were wrong, which rule did you miss?

2 + 3 * 4 ** 2 - 10 / 5 

#WRONG ANSWER ------->
#its wrong to make this calculation without having parenthesis, because the calculations dont follow the right order the result will be different.
#My prediction is 22, but when i print without parenthesis the calculation gives a result of 
# The correct way in order to run this programm is the following.



print(2 + 3 * 4 ** 2 - 10 / 5)

x= 2 + (3 * (4 ** 2)) - (10 / 5)
print(x) 


#CORRECT ANSWER : This prints 48.0, the same as your version with parentheses. 
#Python applies the precedence rules by itself, so the expression isn’t wrong without parentheses.
#The parentheses only make it easier for you to read.