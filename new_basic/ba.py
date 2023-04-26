# base = int(input("Enter BASE:"))
# per =  int(input("Enter PERPENDICULAR:"))
# hyp = (base**2 + per**2)**0.5
# print("Hypotenuse is", hyp)
# uname=input("enter username: ")
# pwd=input("enter pwd: ")
# if uname=='abc' and pwd == 'xyz':
#     print("welcome Master")
#     print("you are logged in")
# else:
#     print("invalid credentials")
#     print("try again")
# username=input("enter username: ")
# email=input("enter email: ")
# pwd=input("enter pwd: ")
# cpwd=input("conferm pwd: ")
# if len(username) > 0 and username.isalnum():
#     if len(email) > 0 and '@'in email:
#         if len(pwd) >=4 :
#             if pwd == cpwd :
#                 print("registration succssfull")
#             else:
#                 print("pwd do not mtched")
#         else:
#             print("pwd must be 4 characters")
#     else:
#         print("invalid email")
# else:
# #     print("invalid pwd")
# x=12
# if x % 2!=0:
#     print("odd")
# marks=int(input("enter your marks: "))
# if marks >= 90:
#     print("Grade A+")
# elif marks >=75:
#     print("Grade A")
# elif marks >=60:
#     print("Grade B")
# elif marks >=55:
#     print("Grade C") 
# else:
#     print("Fail")
# p=int(input("enter the principle--> "))
# r=float(input("enter the rate--> "))
# t=int(input("enter the time--> "))
# si=p*r*t/100
# print("simple intrest is-->>",si)
# data= ""
# while True:
#   line=input(">>>> ")
#   data +=line + ' '
#   if len(line)==0:
#     break
# print(data)
# with open('storybook1.txt','w') as file:
#   file.write(data)
 
# import random 

# print("Random number generator")
# print("enter y to genterate new random number ")
# while input('generate [y/n]):')=='y':
#     number =random.randint(1000,9999)
#     print(f'luckey number:{number}')
# print('Thanks for using')
# import random

# print("random number generator")
# print("enter y to generate new random number ")
# while input("generate [y/n]:")=='y':
#     number  = random.randint(1000,9999)
#     print(f'luckey number:{number}')
# print("Thanks for using")
# a=print("enter the number: ")
# b=print("enter another number: ")
# if a.isnumeric() and b.isnumeric():
#     a,b=int(a),int(b)
#     c=a+b
#     print("the number is: ",c)
# else:
#    print("please enter numbers only")
# data=input("enter a sentence")
# for word in data.split():
#     print(word)
# text='my dog breed name is germanshephard'
# output=''
# for word in text.split:
#     output +=f'{word}aye'
# print(output)
# count=0
# sum=0
# while count <=10:
#     sum=sum+count
#     count = count+1
# # print("sum of 10 consicutive no: ",sum)
# num=int(input("enter the number: "))
# x=num
# sum=0
# rem=0
# while num >0:
#     rem=num %10
#     num=num//10
#     sum=sum+rem
# print("sum of the digits of an entered number", x,"is= ",sum) 
# data="once upon a time in goa there was a crane lived on beach "
# for word in data.split():
# #     print(word)
# num=int(input("enter the number: "))
# x=num
# rev=0
# while num > 0:
#     rem=num %10
#     num=num//10
#     rev=rev*10+rem
# print("the reverse of entered number", x,"is: ",rev)

# num=int(input("enter the number: "))
# x=num
# rev=0
# while num > 0:
#     rem=num %10
#     num=num//10
#     rev=rev*10+rem 
# print("Reverse of entered number",x ,"is=",rev)
# count=1
# sum=0
# while count <=20:
#     if count %5==0:
#         sum=sum+count
#     count=count+1
# print("the sum of number from 1 to 20 is divisible by 5 is: ",sum)
# num=int(input("enter the number: "))
# fact=1
# ans=1
# while fact <= num:
#     ans = ans * fact
#     fact = fact + 1
# # print("the factorial of",num, "is: ",num)
# num=int(input("enter the number: "))
# sum=0
# x=num
# while num > 0:
#     d=num%10
#     num=num//10
#     sum=sum+(d*d*d)
# if (sum==num):
#     print("the number",x,"is Armstrong")
# else:
#     print("the number ",x,"is not Armstrong")
#list 
# x=[]
# x.append(3)
# x.append(5)
# print(x)
# for i in range(11,17):
#     x.append(i)
# print(x)
# y=[23,34,44]
# x.append(y)
# print(x)
# x.extend(y)
# print(x)
# x.insert(1,9)
# print(x)
# x.insert(10,'Hello')
# print(x)
# x.insert(18,[2,5,5,2])
# print(x)
# x=[1,2,3,4,5]
# y=x*2
# print(y)
# x=[1,2,3,4]
# y=[4,5,6,7]
# c=x+y
# print(c)
# # del(x,y)
# del(x[0])
# # print(x)
# z=[]
# a=[1,2,3,4]
# b=[6,7,8,9]
# for i ,j in zip(a,b):
#     ans=i+j
#     z.append(ans)
# print(a)
# print(b)
# print('-' * 15)
# # print(z)
# areas=[]
# length=[2,3,4,5]
# width=[1,2,3,5]
# areas=[l*w for l,w in zip(length,width)]
# print(areas) 
# x=[1,2,3,4,5,6]
# x2=[i**2 for i in x]
# print(x)
# print(x2)
# num=[1,2,3,4,5]
# square=[i**2 for i in num]
# print(square)
# x=[6,45,3,7,86,4,56,7,999,5,3]
# x_even=[i for i in x if i%2==0]
# print(x)
# print(x_even)
# words=['hello','alphabets','goods']
# sizes=[words for w in words]
# print(words)
# # print(sizes)
# words=['alphabet','python','neon','elonmusk']
# sizes=[]
# for w in words:
#     sizes.append(len(words))
# print(words)
# # print(sizes)
# x=[1,2,3,4,5,6,6,'hola','odin']
# if 'hola' in  x :
#     x.remove('hola')
# # print(x)
# print("number from 1 to 10 in reverse order: ")
# for i in range(10,0,-1):
#     print(i,end=" ")
# # print("\n End of Program ")
# print("star pattern display")
# num=7
# x=num
# for i in range(1,6,1):
#     num=num-1;  
# for j in range(1,num, 1):
#     print(" * ",end=" ")
#     x=num-1
# print()
# print("end of program")    
# import pandas as pd 
# import streamlit as st
# import plotly.express as px

# st.page_config(
#     page_title="Pokemon",
#     page_icon="🐉🐱",
#     layout= 'wide',
# )
# st.sidebar.title("🐉 Pokemon App")
# st.image('PAP/Pokemon.jpg',use_columnwidth=True)
# #load data
# def load_Pokemon():
#     pd.read_csv("PAP/pokemon.csv",index_col=True)
#     return Data
# with st.spinner("loading Pokemon data..."):
#     pokemon=load_Pokemon()
#     st.sidebar.success("loading Pokemon data...")

# show_data=st.sidebar.checkbox("show the dataset")
# if show_data:
#     st.subheader("Pokemon Data")
#     st.dataframe(pokemon,use_container_width=True)

# type1=st.sidebar.selectbox('select  Pokemon type',pokemon['Type1'].unique())
# subset=pokemon[pokemon['Type1']==type1]

# quantity = 267
# itemno = 233
# price= 290

# myorder="I want {} pieces of item {} for {} dollers"
# print(myorder.format(quantity,itemno,price))
# class myclass():
#     def _len_(self):
#         return 0

# myobj=myclass()
# print(bool(myobj))

# class myclass():
#     def _len_(self):
#         return 0
    
# myobj = myclass()
# # print(bool(myobj))
# colors=['red','green','yellow']
# for color in colors:
#     print('i like',color)

# for i in range(10):
#     print(i)

# for i in range(100):
# #     print(i,end=' ')  
# for i in range(5,100,20):
#     print(i,end=' ') 
# number=[2,33,4,55,64,23,56,46,77,9,88]
# for i in number:
#     if i % 2==0:
#         print(f'{i} number is even')
#     else:
#         print(f'{i} number is odd')
# colors=['red','green','yellow','blue']
# for color in colors:
#     if 'e' in color:
#         print(color)
# guests=['Er.Amrit','Dr.joseph','mrs.sameera','mr.Ashutosh','Alex']
# for name in guests:
#     if name.startswith('mrs.'):
#         print("hello ma'am")
#     elif name.startswith('mr.'):
#         print("hello sir") 
#     elif name.startswith('Dr.'):
#         print('hello doctor')
#     elif name.startswith('Er.'):
#         print("hello engineer")
#     else:
#         print('invalid invetiation')
# number=[23,33,44,3,42,21,43,56,65,46,66,7,8,87,98,78,64,34,22,68,88]
# for i in number:
#     if i<   30:
#         print('😀')
#     elif i > 50:
#         print('😘')
# else:
#     print('😂')
# import numpy as np

# x=np.array[]
skipfooter?
