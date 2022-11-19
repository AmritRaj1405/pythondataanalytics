ques='what is an Elephant?'
oA="an insect"
oB="a mammal"
oC="reptile"
oD="a bird"
correct='B'

print("welcome to the quiz")
print('-' * 20)
print(f'a) {oA}')
print(f'b) {oB}')
print(f'C) {oC}')
print(f'd) {oD}')
print("ques")
ans=input("enter your ans:")
if ans.upper() == correct:
    print('correct ✔')
else:
    print('incorrect ')