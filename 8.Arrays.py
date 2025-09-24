import array as arr
Numbers = arr.array('i',[1,2,3,4,5,6])
print(type(Numbers))
Numbers.append(8)
print(Numbers)
Numbers.insert(2,6)
print(Numbers)
Numbers.pop(2)
print(Numbers)
Numbers.remove(1)
print(Numbers)

# updating an element
Numbers[0] = 10
print(Numbers)
print(len(Numbers))


