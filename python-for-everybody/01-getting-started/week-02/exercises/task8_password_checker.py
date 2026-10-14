#Mini project: Password checker (everything combined)
#Write a function check_password(pw) that returns a list of problems: too short (under 8), no digit, no uppercase letter.
#Loop: ask for a password until the user enters a valid one or types “done”.
#If there are problems, print each one with an f-string. If valid, print a success message and the number of attempts.
#Hint: look up .isdigit() and .isupper(), and think about looping over the characters.

def check_password(pw):
    problems = []
    if len(pw) < 8:
        problems.append("too short (under 8 characters)")

    has_digit = False
    has_upper = False
    for char in pw:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    if not has_digit:
        problems.append("no digit")
    if not has_upper:
        problems.append("no uppercase letter")
    return problems

attempts = 0
while True:
    pw = input("Enter a password (or 'done'): ")
    if pw == "done":
        break
    attempts = attempts + 1
    problems = check_password(pw)
    if problems:
        for problem in problems:
            print(f"Problem: {problem}")
    else:
        print(f"Password accepted after {attempts} attempt(s)!")
        break

# Part 1: the function

# problems = [] starts an empty list. Every issue found gets added to it, and an empty list at the end means no problems.
# len(pw) < 8 checks the length. If it’s too short, .append(...) adds a message to the list.
# has_digit = False and has_upper = False are flags, meaning “not found yet”.
# for char in pw: loops over the password one character at a time.
# char.isdigit() is True for 0-9, and char.isupper() is True for capital letters. When one is found, its flag becomes True.
# After the loop, if not has_digit: means “the flag is still False”, so a problem gets added. The same applies to uppercase.
# return problems hands the list back. The function never prints anything, it only returns.


# Part 2: the main loop

# attempts = 0 is the counter, and it starts before the loop (the same lesson as count in Task 5).
# while True: keeps asking until a break.
# if pw == "done": break is the exit. It comes before the counter, so typing done doesn’t count as an attempt.
# attempts = attempts + 1 counts each real try.
# problems = check_password(pw) calls your function and stores the returned list.
# if problems: is True when the list has items, because an empty list counts as False. So this means “there is at least one problem”.
# for problem in problems: prints every problem on its own line, with an f-string.
# else: means the list was empty, so the password is valid. It prints the success message with the attempt count, and break ends the loop.

# Test:

# abc gives all 3 problems.
# abcdefgh1 gives only “no uppercase letter”.
# Abcdefg1 is valid, and so is Abcdefgh1 (accepted after however many tries).
# done at any point stops the program.