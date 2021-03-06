
a = '_hello A_'
b = '_world B_'

print('\n',"############ slice  ###########") 
# print(a[1:-1],'1:-1')        # slice
# print(a[0:-1],'0:-1')        # slice
# print(a[-1:9],'-1:9')        # slice
# print(a[0:1009], '0:1009')   # slice
# print(a[-2:-2],'-2:-2')      # slice
# print(a[-0:0],'-0:0')        # slice
# print(a[3:-3],'3:-3')        # slice
# print(a[1:-6],'1:-8')        # slice

#
# https://habr.com/ru/post/89456/
# Все эти действия можно проворачивать со строками, кортежами и списками.
#

s = [1, 2, 3, 4, 6, 55,56,57,58,59] #простой список
#s = "God saw I was dog"
s[:] #копия списка, часто очень полезно
# [1, 2, 3, 4, 6]
print(s[:],' s[:] - копия списка, часто очень полезно')

s[1:] # все элементы кроме первого
# [2, 3, 4, 6]
print(s[1:],' s[1:] - все элементы кроме первого')

s[-3:] # последние 3 элемента
# [3, 4, 6]
print(s[-3:],' s[-3:] # последние 3 элемента')

s[2:-2] #откидываем первые и последние 2
# [3]
print(s[2:-2],' s[2:-2] #откидываем первые и последние 2')

print(s[::2],'парные элементы') #парные элементы
# [1, 3, 6]

print(s[1:4:2],'элементы с первого по четвертый с шагом 2') #элементы с первого по четвертый с шагом 2
# [2, 4]

###
# Слайсы можно удалять, например:
s = list(range(10)) #заполняем 0..9
print(s[:],'выводим слайс')
del s[3: -2: 2] #удаляем элементы между третьим и предпоследним с шагом 2
print(s[:],'выводим слайс')

# Ещё можно вставлять элементы:
s[2:5:2]=list("AF") #список был [0, 1, 2, 4, 6, 8, 9], мы заменили указанные элементы на [‘A’,’F’]
#да, ещё в такой конструкции должны совпадать размеры, это легче понять попробовав
print(s[:],'выводим слайс')
# [ 0, 1, 'A', 4, 'F', 8, 9]

#  вариант вставки попроще:
s[3:4] = ["4 was here"] # замена последовательного кусочка
print(s[:],'замена последовательного кусочка')

s[1:1] = ["after zero"] #или, просто, вставка
print('\n',s[:],'или, просто, вставка')
