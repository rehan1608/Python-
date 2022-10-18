                                                        #---Happy Learning---#
import datetime
def getdate():
    return datetime.datetime.now()
def take_input(t):
    if t==1:
        a=int(input("Enter 1 for food and 2 for exercise : "))
        if a==1:
            value=input("Type your requirement below \n")
            with open("harr_food.txt","a") as h:
                h.write(str([str(getdate)])+": "+value+"\n")
                print("Successfully Added")
        elif a==2:
            value = input("Type your requirement below \n")
            with open("harry_ex.txt", "a") as h:
                h.write(str([str(getdate)]) + ": " + value + "\n")
                print("Successfully Added")
    elif t==2 :
        b = int(input("Enter 1 for food and 2 for exercise : "))
        if b == 1:
            value = input("Type your requirement below \n")
            with open("rohan_food.txt", "a") as h:
                h.write(str([str(getdate)]) + ": " + value + "\n")
                print("Successfully Added")
        elif b == 2:
            value = input("Type your requirement below \n")
            with open("rohan_ex.txt", "a") as h:
                h.write(str([str(getdate)]) + ": " + value + "\n")
                print("Successfully Added")
    elif t==3 :
        c = int(input("Enter 1 for food and 2 for exercise : "))
        if c == 1:
            value = input("Type your requirement below \n")
            with open("hammad_food.txt", "a") as h:
                h.write(str([str(getdate)]) + ": " + value + "\n")
                print("Successfully Added")
        elif c == 2:
            value = input("Type your requirement below \n")
            with open("hammad_ex.txt", "a") as h:
                h.write(str([str(getdate)]) + ": " + value + "\n")
                print("Successfully Added")
        else :
            print("Enter the right keyword 1--Harry, 2--Rohan, 3--Hammad")
def retrive(t):
    if t==1 :
        x=int(input("Enter 1 for food and 2 for exercise : "))
        if x==1 :
            with open("harr_food.txt") as h :
                for i in h :
                    print(i,end=" ")
        elif t==2 :
            with open("harry_ex.txt") as h :
                for i in h :
                    print(i,end=" ")
    elif t==2 :
        x = int(input("Enter 1 for food and 2 for exercise : "))
        if x == 1:
            with open("rohan_food.txt") as h:
                for i in h:
                    print(i, end=" ")
        elif t == 2:
            with open("rohan_ex.txt") as h:
                for i in h:
                    print(i, end=" ")
    elif t==3 :
        x = int(input("Enter 1 for food and 2 for exercise : "))
        if x == 1:
            with open("hammad_food.txt") as h:
                for i in h:
                    print(i, end=" ")
        elif t == 2:
            with open("hammad_ex.txt") as h:
                for i in h:
                    print(i, end=" ")
    else :
        print("Enter the right keyword 1--Harry, 2--Rohan, 3--Hammad")
print("This is a health Management system")
z=int(input("Enter 1 for log the value and 2 for retrive the value : "))
if z==1 :
    xx=int(input("Enter 1--Harry, 2--Rohan, 3--Hammad : "))
    take_input(xx)
elif z==2 :
    xx = int(input("Enter 1--Harry, 2--Rohan, 3--Hammad : "))
    retrive(xx)
