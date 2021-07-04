#HangMan
from random import randint


Wlist=["word","language","melody","world","tower","python","master","devil","mobile","remote","baker","horizen","mean",
"festival","beautiful","dangerous","airplane","modify","monster","people","children"]

def start():
    playermode=int(input("For 2 player mode enter '2' or for single player mode enter '1' : "))
    point=0
    if playermode==1:
        rand=randint(0,(len(Wlist)-1))
        selword=Wlist[rand]
        draw(point)
        combfinder(selword,point)
    elif playermode==2:
        word=input("Player 1, please input the Word: ").lower()
        if word not in Wlist:
            Wlist.append(word)
            print(Wlist)
        print(chr(27),"[2J")
        draw(point)
        combfinder(word,point)
    else:
        print("player mode not selected correctly")


        


def draw(point):#drawing hang man
    L=["         _____________ ","        |             |      ","                      |      ","                      |      ",
    "                      |      ","                      |      ","                      |      ","                      |      ",
    "                      |      ","                      |      ","                      |      ","                  ____|____"]
    
    if point==0:
        for i in L:
            print(i)
    if point>0:#head
        L[2]="       /^\            |"
        L[3]="      <o,o>           |"
        L[4]=r"       \"/            |"
        
        if point>1:#body
            L[5]="      =[ ]=           |"
            L[6]="       [ ]            |"
            L[7]="       ( )            |"
            
        if point==3:#left arm
            L[5]=r"      =[ ]=\\         |"
            L[6]=r"       [ ]  \\        |"
            L[7]="       ( )   \~_,     |"
            
        if point>3:#right arm
            L[5]=r"    //=[ ]=\\         |"
            L[6]=r"   //  [ ]  \\        |"
            L[7]=r",_~/   ( )   \~_,     |"
            
            if point==5:#left foot
                L[8]=r"         \\           |"
                L[9]=r"          \\          |"
                L[10]=r"           \\         |"
                L[11]=r"            \~_>  ____|____"
                
            if point==6:#right foot
                L[8]=r"      // \\           |"
                L[9]=r"     //   \\          |"
                L[10]=r"    //     \\         |"
                L[11]=r" <_~/       \~_>  ____|____"
    
        for i in L:
            print(i)
                

    
        

def combfinder(word,po):
    point=po
    leng=len(word)
    Word=leng*["_"]
    print(Word)
    while True:
        letter=input("player 2,Geuss any letter: ").lower()
        if letter in word:
            for l in range(len(word)):
                if word[l]==letter:
                    Word[l]=letter
                    
        else:
            point+=1
            if point==6:
                draw(point)
                print("Game Over!,You Faild to guess the Word\n The word was",word)

                break

        print(chr(27),"[2J")
        draw(point)
        print(Word)
        
        if "_" not in Word:
            print("Congratulations!")
            break


start()






   