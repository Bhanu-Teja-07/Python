s="Integer Number".strip(" ")
fre={}
for i in s:
    if i in fre:
        fre[i]+=1
    else:       
        fre[i]=1
print(fre)
