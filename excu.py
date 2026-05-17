def vowels(s):
    s=s.lower()
    count=0
    v=['a','e','i','o','u']
    for char in s:
        if char in v:
            count+=1
    return count

def mark(marks):
    if marks >90:
        print("grade A")
    elif marks >=80:
        print("grade B")
    elif marks>=70:
        print("grade C")
    elif marks >=60:
        print("grade B")
    else:
        print("fail")
marks=int(input())
mark(marks)