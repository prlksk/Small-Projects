import random
x=random.randint(1,20)
print("i am thinking")
for guessTaken in range(1,21):
    g=int(input())
    if g<x:
        print("it is too small.Please choose a bigger one")
    elif g>x:
        print("it is too big.Please choose a smaller one")
    elif x==g:
        print("the right number")
    else:
        break
if guess==secretNumber:
    print("good job.{}ndefada bildin".format(guessTaken))
else:
    print("ups,you are not right")

'''f="ajgljfskngfsdjgk"

for i in range(5):
    b=random.randint(0,len(f))
    r=random.randint(0,len(f))
    print(f[b:r])
collat

x=int(input("sayı gir"))
sayi=0
while x>1:
    if x%2==0:
         x=x/2
         sayi=x
        
    elif x%2!=0:
          x= 3*x+1
          sayi=x
    print(sayi)'''
    
