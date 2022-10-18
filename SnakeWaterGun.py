while (True):
    import random
    print("\t\tLet's play the famous game")
    n=1
    chances=9
    comp_score = 0
    user_score = 0
    while (n<=10):
        comp_t=0
        user_t=0
        a=["Snake","Water","Gun"]
        choice=random.choice(a)
        b=input("Enter 'S' for 'Snake', 'W' for 'Water' and 'G' for 'Gun' : \n\t")
        user=b.capitalize()
        if (choice=="Snake" and user=="W") or (choice=="Gun" and user=="S") or (choice=="Water" and user=="G") :
            print("You lost!")
            user_score = user_score + 0
            comp_score = comp_score + 10
        elif (choice=="Snake" and user=="G") or (choice=="Water" and user=="S") or (choice=="Gun" and user=="W") :
            print("You Won!")
            user_score = user_score + 10
            comp_score = comp_score + 0
        elif (choice==user) :
            print("You both selected the same ")
        else :
            print("Please Enter the right value")
        print("Chances left", chances)
        chances=chances-1
        n=n+1
        user_t = user_t + user_score
        print("\tYour total :", user_t)
        comp_t = comp_score + comp_t
        print("\tOpponent total :", comp_t)
    if user_t>comp_t :
        print("\tHuureh! You won the final")
    elif user_t<comp_t :
        print("\tOops! You lost the game, You can play again")
    else :
        print("\tYou both scored the same")
    print()
    x=input("Enter 'Y' to play again and any other key to exit : ")
    y=x.capitalize()
    if y=="Y":
        print()
        continue
    else:
        break
