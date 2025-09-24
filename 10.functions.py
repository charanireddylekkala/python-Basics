def greet(name,branch):
    print("Hello world1",name,branch)
greet("charani","cse&aiml") #calling function
name = "charani"
print("hello",name)
#positional arguments
def greet(rollno,name):
    print("hello",name,"your rollno is",rollno)
greet("f7","charani")
#keyword argument
def greet(name,rollno):
    print("hello",name,"your rollno is",rollno)
greet(name ="charani",rollno ="f7")
#default agument
def greet(name = "student"):
    print("hello",name)
greet()
greet(name ="charani")
#variable-length arguments
#L = 10,20,30,40,50
def sum1(*List1):
    sum2 = 0
    for i in range(len(List1)):
        sum2 = sum2+List1[i]
    print(sum2)
sum1(10,20,30,40,50)
def details(**info):
    for i,j in info.items():
        print(i,":",j)
details(name="charani",rollno="f7",branch="csm")
x=10
def var1():
    y = 5
    print ("inside var1 function",x,y)
var1()
def var2():
    print("inside var2 function",x)
var2()

print("outside function",x)
#lambda function
def sqe(a):
    print(a*a)
sqe(5)










