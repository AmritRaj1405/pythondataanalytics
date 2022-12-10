msg='journey before destination'
msg_upr=msg.upper()
print(msg)
print(msg_upr)
#msg_lower=msg.lower()
#print(msg_lower)
msg_cap=msg.capitalize()
#msg_title=msg.title()
#msg_swp=msg.swapcase()
#msg_cf=msg.casefold()#same as lower case
print(msg_cap)
#print(msg_title)
#print(msg_cf)
print(msg.ljust(100,'|'))
print(msg.rjust(100))
print(msg.center(100,'-'))
#alligment with 'f' string
print(f"{msg:>50}")#same as rjust
print(f"{msg:<50}")#same as ljust
print(f"{msg:^50}")#same as center