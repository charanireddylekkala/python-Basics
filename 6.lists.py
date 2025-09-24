#count even and odd numbers
a=[2,55,99,7,6,23,44,48,52,77,62,]
evn_cnt=0
odd_cnt=0
for i in a:
    if i%2==0:
        evn_cnt +=1
    else:
        odd_cnt +=1

        print("Number of even numbers in the list:",evn_cnt)
        print("Number of odd numbers in the list:",odd_cnt)
#Multiply each element with 2 in the list
a=[-2,5,-99,-7,6,23,-44,48,52,-77,62,-61]
b=[]
for i in a:
    b.append(i*2)