# 01-getting-started - Week 2

## Τι έμαθα

## Παράδειγμα κώδικα

                                        **Monday 12/10/2026**
Review day : Practice with claude of what i did the previous week writing mini projects(summury of the 1st course), before i move to course 02-data-structures.


                                        **Wednesday 14/10/2026**
Review day : Claude tasks practice. 
for i in range(5):
     print(i)    #i= 0 1 2 3 4          So range(5) starts 0 and stops before 5

 for i in range(1,6):
     print(i)            #i= 1 2 3 4 5

 for i in range(5, 0, -1):
     print(i)              #i= 5 4 3 2 1 (the three numbers are start, stop, step, and -1 means “go down by 1”.)
                            5 is where it starts.
                             0 is where it stops, but the stop value is never printed. Python goes until it reaches 0, then quits before printing it.
                            -1 is how much it changes each time. So it goes 5, 4, 3, 2, 1, and when the next value would be 0, it stops.


print(f"{name} costs {items[name]:.2f}")
It’s a format spec inside the { } of an f-string:

   : starts the format spec.
    .2 means 2 digits after the decimal point.
    f means format as a float (a decimal number).

Examples:

f"{3.5:.2f}" gives 3.50
f"{2.9985:.2f}" gives 3.00 (it rounds)
f"{7:.2f}" gives 7.00

It always shows exactly 2 decimals, which is why it’s the right choice for money. For other digit counts, change the number: :.1f gives 1 decimal, :.0f gives none.