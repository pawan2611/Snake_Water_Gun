you=0
comp=0
trials=0
TIE=0

def win():
    import random
    lst=["S","W","G"]
    choice1=random.choice(lst)
    choice2=input("ENTER YOUR CHOICE IN CAPS\n('S' FOR SNAKE\n'W' FOR WATER\n'G' FOR GUN):")
    print("MY CHOICE WAS",choice1)
    
    global you,comp,TIE
    if choice1==choice2:
        print("ROUND TIEED")
        TIE+=1
    else:
        if choice1=="S" and choice2=="W":
            print("I WON THE ROUND")
            comp+=1
        elif choice1=="S" and choice2=="G":
            print("YOU WON THE ROUND")
            you+=1
        elif choice1=="W" and choice2=="G":
            print("I WON THE ROUND")
            comp+=1
        elif choice1=="W" and choice2=="S":
            print("YOU WON THE ROUND")
            you+=1
        elif choice1=="G" and choice2=="S":
            print("I WON THE ROUND")
            comp+=1
        elif choice1=="G" and choice2=="W":
            print("YOU WON THE ROUND")
            you+=1
    
while trials<10:
    win()
    trials+=1
print()
print("MY SCORE=",comp,"\nYOUR SCORE=",you,"\nTIED ROUNDS=",TIE)
if comp>you:
    print("I WON THE GAME")
elif comp<you:
    print("YOU WON THE GAME")
else:
    print("GAME TIED")
