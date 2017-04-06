from random import randint
d={1,2,3,4,5,6}
def score():
    print "start the batting"
    score=0
    while True:
        run=input()
        ball=randint(1,6)
        if run not in d:
            print "invalid"
            exit()
        elif run!= ball:
            score+=run
        else:
            print "you are out"
            print "your score was ",score
            break
    return score
def secbowl(target):
    print "computer need=",target+1
    run=0
    while True:
        ball=input()
        bat=randint(1,6)
        if run>target:
            print "computer won the match"
            break
        elif ball!=bat:
            run+=bat
            if run>target:
                print "computer won"
                break
            print "its was a",bat
        else:
            if run == target:
                print "match draw"
                break
            elif run < target:
                print "user u have won the match"
                break
            else:
                print "computer won"
                break
def firbowl():
    print "lets start the bowling"
    run=0
    while True:
        ball=input()
        bat=randint(1,6)
        if ball not in d:
            print "invalid"
            exit()
        elif ball!=bat:
            run+=bat
            print "it was a ",bat
        else:
            print  "thatzz a wicket"
            print "user u need runs of ",run+1
            break
    return run
def chase(target):
    print "play the chasing"
    run=0
    while True:
        bat=input()
        bowl=randint(1,6)
        if bat not in d:
            print "invalid"
            exit()
        if run>target:
            print "user u won the match"
            break
        elif bat!=bowl:
            run+=bat
            if run>target:
                print "user u won the match"
                break
        else:
            print "ooo nooo out"
            if run == target:
                print "match draw"
                break
            elif run < target:
                print "u have loss the match"
                break
            else:
                print "computer won"
                break
print "welcome to handcricket"
print "use numbers from 1-6 only "
choice=input("1.even\n2.odd\n")
if choice not in d:
    print "invalid"
elif choice==1:
    user=input("enter\n")
    rand=randint(1,6)
    if user not in d:
        print "invalid"
        exit()
    if((user+rand)%2 ==0):
        print("u won the toss what u what to do first\n 1 for bat \n 2 for bowl")
        position=input()
        if(position==1):
            total=score()
            secbowl(total)
        elif(position==1):
            target=firbowl()
            chase(target)
        else:
            print "invalid"
    else:
        print ("u loss the toss start the bowling")
        target=firbowl()
        chase(target)
elif choice==2:
    user=input("enter")
    rand=randint(1,6)
    if((user+rand)%2!=0):
        print("u won the toss what u what to do first\n 1 for bat \n 2 for bowl")
        position = input()
        if (position == 1):
            total = score()
            secbowl(total)
        elif (position == 2):
            target = firbowl()
            chase(target)
        else:
            print "invalid"
    else:
        print ("u loss the toss start the bowling")
        target = firbowl()
        chase(target)