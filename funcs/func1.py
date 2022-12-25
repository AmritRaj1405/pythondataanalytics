#count a total no of string in  statement
def word_count(sentence):
    word= sentence.split()
    return len (word)
#calling 
print(word_count('hello world!'))
size=word_count("hello world of pain")
print(size)
    

data= input("enter a statement:")
size=word_count(data)
print(f'you entered {size} words')