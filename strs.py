# str() - type
# to check typy of obj usualy use funk type(obj)
# 1. 'str' in single quote
# 2. "str" in double quote
# 3. "'str' in str" or '"str" in str' or '''"str" in str'''to use some quote in str use ather quote
print("'str' in str") # 'str' in str
print('"str" in str') # "str" in str
print('''"str" in str''') # "str" in str
# function print has several default atributes print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# sep is separator beatween objects, by default is
d = "world with sep=0"
print("hello", d, sep="0") # hello0world with sep=0
print("hello world with sep=0", sep='0') # hello world with sep=0
# ather is end, in the end of str + \n
print('Line break normal') # Line break normal
print('Line break = double', end='\n'*2) # Line break = double
#
print('Line break = "USA"', end='USA') # Line break = "USA"USA
# some game with print()
print('hello', 'world', 'my', 'friend', sep=' ')
print('hello', 'world', 'my', 'friend', sep='T')
print('hello'+'world'+'my'+'friend', sep='T')
a = 'helo'
b = 'world'
print(a, b) # print two values
print(a+b) # add two str
print(a or b) # show only value True
print(a and b) # show you list item if before were True
print(a*2)
print(a[1:-1]) # slice
print(1+6) # any number expression
def hello():
return 'hello'
print(hello())# you can put funktion in print or any ather object which has return str value, now will print hello
def world():
text='world'
print(world()) # None


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