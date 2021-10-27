import random
def gamewin(comp,you):
    if comp=='s':
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
print("computer turn: Snake(s) Water(w) Gun(g)")
randnum=random.randint(1, 3)
if randnum==1:
    comp='s'
elif randnum==2:
    comp='w'
elif randnum==3:
    comp='g'    
you=input("Your turn: Snake(s) Water(w) Gun(g)")

print("Computer chooses",comp)
print("You chooses",you)
if you==comp:
    print("Tie")
elif you:
    print("Win")
else:
    print("losse")    
print("     !Thank you for playing")
