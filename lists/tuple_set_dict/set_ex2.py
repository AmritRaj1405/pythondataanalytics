x={1,2,3,4,5}
y={4,5,6,7,8,9,10}

print(x)
print(y)
print(x | y)#same as x.union(y)
print('intersection')
print(x & y)#same as x.intersection(y)
print('difference')
print("unique value in x=>", x-y)#same as x.difference(y)
print("unique values in y=>",y-x)
print('symmetric diffeence')
print(x ^ y)#same as x.symmetric_difference(y)
z={10,11,12,13}
print('disjoint sets')
print('disjont sets')
print("kya x or y me kuch bhi common nhi h =>",x.isdisjoint(y))
print("kya x or z me kuch bhi common nhi h =>",x.isdisjoint(z))
print("kya z or y me kuch bhi common nhi h =>",x.isdisjoint(y))


items={'apple','orange','banana','mango'}
fruits={'apple','orange','banana'}
vegitables={'apple','orange','banana','cucumber'}

print('subset')
print('fruits belongs to items',fruits.issubset(items))
print('fruits belongs to items',vegitables.issubset(items))

