import random
l=['hangman','xylophone','pokemon','apple','king']
c=0
n=random.randint(0,4)
s=l[n]
l1=[]
while c<6:
    s1=input("Enter letter:")
    l1.append(s1)
    if s1 in s:
        if s.find(s1)==0:
            print(s,'in 1st position')
        elif s.find(s1)==1:
            print(s,'in 2nd position')
        else:
            print(s1,' in ',s.find(s1)+1,'th positon',sep='')
    else:
        print(s1,'not found')
        c+=1
    d=''
    for i in s:
        if i in l1:
            d+=i+' '
        else:
            d+='_'
    print(d.strip())
    if all(i in l1 for i in s):
        print("You guessed the word")
        break
else:
    print(f"You lost, the word was:{s}")
