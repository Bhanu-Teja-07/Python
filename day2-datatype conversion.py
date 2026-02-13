'''
#read the input from the user
num = int(input("Enter the value: "))
print(num)
print(type(num))

#implict type conversion
num1 = float(input("Enter the float value: "))
print(num1)
print(type(num1))
res=num1+num
print(res)
print(type(res))

#to overcome the error we need to convert the string to int or float
num1=input()
print(type(num1))
res=int(num1)+10
print(res)
print(type(res))
'''
#converting integer to float,string and boolean
num2=10
print(float(num2))
print(str(num2))
print(bool(num2))
print(len(str(num2)))