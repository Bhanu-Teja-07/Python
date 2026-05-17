students=int(input("Enter the number of students : "))
T=list(map(int,input().split()))
E=list(map(int,input().split()))
H=list(map(int,input().split()))
Sc=list(map(int,input().split()))
So=list(map(int,input().split()))
tot=[]
student_names=list(map(str,input().split()))
for i in range (students):
    tot.append(T[i]+E[i]+H[i]+Sc[i]+So[i])
maxi=max(tot)
ind=tot.index(maxi)
print("marks of ",student_names[ind],":",maxi)

