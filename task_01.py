# num = [1, 4, 4, 7, 11, 2, 1, 5]
# print(num)
# lst = []
# for i in num:
#     if i not in lst:
#         lst.append(i)
# print(lst)


num = list(map(int, input('Введите числа через пробел: --> ').split()))  

print(f'{num}')
lst = []
num = [lst.append(i) for i in num if i not in lst] 
print(f'{lst}')