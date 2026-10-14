#Grade function (functions, return, elif)
#Write a function get_grade(score) that returns “A” (90+), “B” (80+), “C” (70+), or “F”. Call it with 3 different scores and print the results.

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

s1=get_grade(95)
s2=get_grade(82)
s3=get_grade(50)
print(s1)
print(s2)
print(s3)




