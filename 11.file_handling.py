file = open("student.txt","r")
content=file.read()
print(content)
file.close()
#2.readlines
file = open("student.txt","r")
content=file.readline()
content1=file.readline()
content2=file.readline()
content3=file.readline()
print(content)
print(content1)
print(content2)
print(content3)
#write
file = open("student.txt","w")
file.write("hello c++\n")
file.write("hello python\n")
lines = ["hello charani\n","hello sarayu\n","hello world\n"]
file.writelines(lines)
file.close()






