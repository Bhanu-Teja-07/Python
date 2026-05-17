'''s="codegnan"
print(s[0])
print(s[0:5])
print(s[5:8:-1])
print(s[8:4:-1])
print(s[-1:5])
print(s[0::1])'''

n=int(input())
absent=0
present=0
for i in range(1,n+1):
    val=int(input("Enter the roll number {i} attendance:"))
    if val==0:
        absent+=1
    else:        
        present+=1
print("present:",present)
print("absent:",absent)
print ("present average :",(present/n)*100)