def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1//num2
def sqroot(num1,num2):
    return num1**num2
inputing=int(input("enter 1 for add , enter 2 for sub  , enter 3 for mul , enter 4 for div , enter 5 for sqroot: "))
input1=int(input("enter numnber 1: "))
input2=int(input("enter the second number or the exponent: "))
if inputing == 1:
    print(add(input1,input2))
elif inputing== 2:
    print(sub(input1,input2))
elif inputing == 3:
    print(mul(input1,input2))
elif inputing==4:
    print(div(input1,input2))
elif inputing ==5:
    print(sqroot(input1,input2))
else:
    print("ERROR:  wrong selection input")