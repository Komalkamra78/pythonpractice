from operator import truediv
import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
   

print("comp turn: Snake(s),Water(w), or Gun(g)?")
randNO= random.randint(1,3)
# print(randNO)
if randNO == 1:
    comp = "s"
elif randNO == 2:
    comp = "w"
elif randNO == 3:
    comp = "g"

you = input("your turn : Snake(s) , Water(w) or Gun(g)?")
a = gamewin(comp, you)

print(f"computer choose: {comp}")
print(f"you choose: {you}")
if a == None:
    print("the game is a tie!")
elif a:
    print("you win!!")
else:
    print("computer win the game.you lost!")

  