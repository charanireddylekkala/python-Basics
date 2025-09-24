My_dict = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    "key4":"value4",
}
print(My_dict)
A = {"n" :"charani","n1":"akhil"}
print(A)
B={
    6:"value1",
    3.5:"value2",
    "key3":"value3"
}
print(B)
Biodata ={
    "name":"charani",
    "class":"1st year",
    "branch":"csm",
    "roll no":"f7",
}
print(Biodata["name"])
print(Biodata["class"])
print(Biodata["branch"])
E_d = {}
print(E_d)
A ={
    "Roll no":"f7",
}
print(A.get("Roll no"))
Biodata["age"] = 24
print(Biodata)
Biodata["place"] = "hyderababad"
print(Biodata)
Biodata.pop("branch")
print(Biodata)
Biodata.popitem()
print(Biodata)
del Biodata ["name"]
print(Biodata)
print(Biodata.keys())
print(Biodata.values())
print(Biodata.items())
Biodata.update({"Role":"web developer","place":"hyderababad"})
print(Biodata)

# loops for dictionary
L = [10,20,30,40]
for i in L:
    print(i)
Biodata ={
    "name ":"charani",
    "branch":"csm",
    "roll no":"f7",
}
for i in Biodata:
    print(i)
for i in Biodata.keys():
    print(i)
for i in Biodata.values():
    print(i)
for i in Biodata.items():
    print(i)
#nested tuple:
T = (10,(20,30),(40,50))
print(T[2][1])
#nested dictionary
students = {
    "s1":{"name":"charani","Roll no":"f7"},
    "s2":{"name":"akhil","Roll no":"f8"}
}
print(students["s1"]["Roll no"])
print(students["s2"]["Roll no"])











