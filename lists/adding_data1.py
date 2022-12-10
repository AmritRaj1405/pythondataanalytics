x=[]
x.append(2)
x.append(5)
print(x)
x.append(10)
print(x)

for i in range(11,17):
    x.append(i)
print(x)
# adding one list to anathor list
y=[22,44,33]
x.extend(y)
print(x)
#adding data at the mid or any position 
x.insert(2,9)
print(x)
x.insert(10,'hello')
print(x)