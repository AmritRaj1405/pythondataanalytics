#find,index,rfind
message='The quick brown fox jumped over the lazy dog'
idx=message.find('own')
if idx!=-1:
    print(f'found "own" at index {idx}')
else:
    print("not found own")
idx=message.find('jump')
if idx!=-1:
    print(f'found "jump" at index {idx}')
else:
    print("not found jump")
idx=message.find("brown")
print(f'found "brown" at index {idx}')
#idx=message.rfind("the")
#print(idx)
