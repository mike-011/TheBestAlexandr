text = 'hel lo'
for i in text:
    print(i) # tab

# func enumerate()
for e,m in enumerate(text): # первая е для цифр функции enumerate() второе m для значения данных из  text
    print(e, m, sep=' - ') # tab

# same without enumerate()
e = 0
for m in text:
    print(e, m, sep = ' - ') # tab
    e+=1 # tab

# слово наоборот
newtext = ''
for l in text:
    newtext = l + newtext # tab
    print(newtext) # tab

# подсчет анных
used_letters = []
for l in text:
    if l in used_letters: # tab
    print(l ,' value for the letter we know') # tab + tab
    else: # tab
    print(l, ' = ', text.count(l)) # tab + tab
    used_letters.append(l) # tab + tab
# double for
# we want to draw chess table
# we want get
# 1a 1b 1c 1d 1e 1f 1g 1h
# 2a 2b 2c 2d 2e 2f 2g 2h
# 3a 3b 3c 3d 3e 3f 3g 3h
# 4a 4b 4c 4d 4e 4f 4g 4h
# 5a 5b 5c 5d 5e 5f 5g 5h
# 6a 6b 6c 6d 6e 6f 6g 6h
# 7a 7b 7c 7d 7e 7f 7g 7h
# 8a 8b 8c 8d 8e 8f 8g 8h
numbers = [1,2,3,4,5,6,7,8]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for n in numbers:
for l in letters: # tab
    print(n, l, end=' ', sep='') # tab + tab
    print() # этот принт для переноса строки он относится к первому for # tab

for n in numbers:
for l in letters: # tab
    if n%2==0 and l in ['a', 'c', 'e', 'g']: # tab + tab
    print(n, l, end=' ', sep='') # tab + tab + tab
    print() # tab