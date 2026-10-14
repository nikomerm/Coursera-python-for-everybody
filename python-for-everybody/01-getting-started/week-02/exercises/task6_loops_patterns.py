#Countdown and pattern (for, range, nested loops)
#a) Print a countdown from 10 to 1, then “Liftoff!”.
#b) Print a triangle of stars with 5 rows (1 star, then 2, and so on).

#Examples to understand the task : 
# for i in range(5):
#     print(i)    #i= 0 1 2 3 4          So range(5) starts 0 and stops before 5

# for i in range(1,6):
#     print(i)            #i= 1 2 3 4 5

# for i in range(5, 0, -1):
#     print(i)              #i= 5 4 3 2 1 (the three numbers are start, stop, step, and -1 means “go down by 1”.)
#                             5 is where it starts.
#                             0 is where it stops, but the stop value is never printed. Python goes until it reaches 0, then quits before printing it.
#                            -1 is how much it changes each time. So it goes 5, 4, 3, 2, 1, and when the next value would be 0, it stops.

for i in range(10,0,-1):
    print(i)
print("Liftoff!")

for s in range(1, 6):
    print("*" * s)

