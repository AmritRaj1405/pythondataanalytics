username=input("enter username")
email=input("enter email")
pwd=input("enter pwd")
cpwd=input('conform pwd')

if len(username)>0 and username.isalnum():
    if len(email)>0 and '@'in email:
        if len(pwd)>=4:
            if pwd == cpwd:
                print("registration successful")
            else:
                print("passward do not match")
        else:
            print("pwd must be at least 4 characters")
    else:
        print('invalid email')
else:
    print('username is invalid')