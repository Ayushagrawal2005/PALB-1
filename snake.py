import random
def check(comp , user):
    if comp == 0 and user == 0:
        return "Draw"
    elif comp == 0 and user == 1:
        return "You Win"
    elif comp == 0 and user == 2:
        return "Computer Wins"
    elif comp == 1 and user == 0:
        return "Computer Wins"
    elif comp == 1 and user == 1:
        return "Draw"
    elif comp == 1 and user == 2:
        return "You Win"
    elif comp == 2 and user == 0:
        return "You Win"
    elif comp == 2 and user == 1:
        return "Computer Wins"
    elif comp == 2 and user == 2:
        return "Draw"
comp = random.randint(0,2)
user = int(input("Enter 0 for Snake, 1 for Water, 2 for Gun: "))
result = check(comp, user)
print(f"Computer chose: {comp}")
print(f"You chose: {user}")
print(result)