pas=input()
upp,low,dig,sym=0,0,0,0
if len(pas)>8:
    for i in range (len(pas)):
        if pas[i].isupper():
            upp+=1
        elif pas[i].islower():
            low+=1
        elif pas[i].isdigit():
            dig+=1   
        elif pas[i] in '!@#$%^&*()-+':
            sym+=1
if upp and low and dig and sym >0 :
    print("the password is strong")
else:
    print("the password is weak")
    