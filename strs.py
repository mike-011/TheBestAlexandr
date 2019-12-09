# str() - type
# to check typy of obj usualy use funk type(obj)
# 1. 'str' in single quote
# 2. "str" in double quote
# 3. "'str' in str" or '"str" in str' or '''"str" in str'''to use some quote in str use ather quote
"""
print('\n','############ str in str ###########') 
print("'str' in str") # 'str' in str
print('"str" in str') # "str" in str
print('''"str" in str''') # "str" in str


# function print has several default atributes print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# sep is separator beatween objects, by default is
print('\n',"############ hello0world with sep=0 ###########") 
d1 = "hello"
d2 = "world"
d3 = "with"
d4 = "sep"
d5 = "same"
d6 = "null"
print("say", d1,d2,d3,d4,d5,d6, sep=" ") # hello0world with sep=0
print("say", d1,d2,d3,d4,d5,d6, sep="0") # hello0world with sep=0
print("say", d1,d2,d3,d4,d5,d6, sep='___') # hello world with sep=0
print("say", d1,d2,d3,d4,d5,d6, sep='-') # hello world with sep=0
print("say", d1,d2,d3,d4,d5,d6, sep='+++') # hello world with sep=0
print("say", d1,d2,d3,d4,d5,d6, sep='') # hello world with sep=0
print("say", d1,d2,d3,d4,d5,d6, sep='      дичь подана       ') # hello world with sep=0

#code for disabling the softspace feature 
print('G','F','G', sep='') 
  
#for formatting a date 
print('09','12','2016', sep='-') 
  
#another example 
print('pratik','geeksforgeeks', sep='@') 

# ather is end, in the end of str + \n
print('\n',"############ Line break normal ###########") 
print('Line break normal') # Line break normal
print('Line break = double', end='ee#@!\n2019'*3) # Line break = double
print('Line with ') # Line break normal

# https://www.geeksforgeeks.org/python-sep-parameter-print/
print('09','12', sep='-', end='-2016\n') 

#
print('\n',"############ Line break = "'USA'" USA ###########") 
print('Line break = "USA"', end='USA') # Line break = "USA"USA

# some game with print()
print('\n',"############ some game with print() ###########") 
print('hello', 'world', 'my', 'friend', sep=' ')
print('hello', 'world', 'my', 'friend', sep='T')
print('hello'+'world','my'+'friend','rr', sep='T')

a = '_hello A_'
b = '_world B_'
c = '_C_'
d = '_D_'
e = '_E_'
f = '_F_'

print('\n',"############ PRINT VAR  ###########") 
print(a,b,c,d,e,f) # print two values
print(a+b+c+d+e+f) # add two str
print(a or b or c or d or e or f) # show only value True
print(a and ((b and c) and (d and e) and f)) # show you list item if before were True
print(a*5)


a = '_hello A_'
b = '_world B_'

print('\n',"############ slice  ###########") 
print(a[1:-1],'1:-1') # slice
print(a[0:-1],'0:-1') # slice
print(a[-1:9],'-1:9') # slice
print(a[0:1009], '0:1009') # slice
print(a[-2:-2],'-2:-2') # slice
print(a[-0:0],'-0:0') # slice
print(a[3:-3],'3:-3') # slice
print(a[1:-6],'1:-8') # slice

print(1+6) # any number expression


print('\n',"############ PRINT FUNCTION  ###########") 
def hello():
    return 'hello'

print(hello())# you can put funktion in print or any ather object which has return str value, now will print hello

def pause():
    wait = input("PRESS ENTER TO CONTINUE.")
    

def world():
    text='world'
    print(text) # None

print(world()) # None <-- RECURSION <--
"""



print('\n',"############ FORMAT  ###########") 
# format
a = '{}'.format('str')

print(a) # str
print('{}'.format('str1')) # str1
print('{}{}'.format('str1','str2')) # str1str2
print('{2}{1}{0}'.format('str1','str2','str3')) # str3str2str1
print('{0}VS{0}'.format('str1')) # str1VSstr1
print('{hello} - {world}'.format(hello='HELLO', world="WWorld")) # HELLO - WWorld  you can add names for vars
print('{hello[1]:} and {world}'.format(hello='Hello', world='World')) # e and World
print('{hello!r} and {world}'.format(hello='Hello', world='World')) # 'Hello' and World
print('{hello!s} and {world}'.format(hello='Hello', world='World')) # Hello and World
print('! {hello:<20} and {world}'.format(hello='Hello', world='World')) # ! Hello                and World
print('! {hello:>20} and {world}'.format(hello='Hello', world='World')) # !                Hello and World
print('! {hello:^20} and {world}'.format(hello='Hello', world='World')) # !        Hello         and World
print('! {hello:*^20} and {world}'.format(hello='Hello', world='World')) # ! *******Hello******** and World

# %
a = '%s'%'Hello'
print(a)
print('Hello %s big %s'%('my', 'world'))
print('Hello %d big %s'%(7, 'world'))

spaces=20
stars = ''

for i in range(0,10,2):
    print('|{text:^{display_width}}|'.format(text=stars, display_width=spaces))
stars = str(i*'*')
