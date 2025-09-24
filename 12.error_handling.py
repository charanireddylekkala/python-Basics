try:
    a = int(input("enter the numerator:"))
    b = int(input("enter the denominator:"))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Error:Division by zero is not possible")
try:
    rollno = int(input("enter your rollno:"))
except valueError:
    print("Error: given value is not in the integer data type.")
try:
    i = 2
    n = int(input("enter the n value:"))
    if i%n==0:
        print("yes,n is multiple of",n)
    else:
        print("no,number is not multiple of ",n)
except ZeroDivisionError:
    print("Error:Division by zero is not possible")
#index error
try:
    List = [10,20,30]#0,1,2
    n = int(input("enter the index value:"))
    print(List[2])
except:
    print("Error: the given index is not from the list")
    #key error
#try:
    #Dict = {"name":"charani"," rollno" :"f7"}
    #print(Dict["age"])
#except keyError:
    #print("Error: the given key is not from the list")
try:
    sum = "5" + 5
    print(sum)
except TypeError:
    print("Invalid type operation.")
#name error
try:
    print(Mult)
except NameError:
    print("variable not declared")
#file NotFoundEroor:
try:
    file = open("detail.txt","w")
    print(file.read())
except:
    print("File is not found in the system.")
finally:
    print("program is excuted")


