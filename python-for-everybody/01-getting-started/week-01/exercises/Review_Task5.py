#Task 5: Comparison and if/else
#Ask the user for a test score. Print Pass if it is 50 or more, otherwise print Fail. Test with 50, since the edge case is where mistakes happen.

tst_score=input("Enter score:")
score=int(tst_score)
if score >= 50:
    print("Pass")
else:
    print("Fail")