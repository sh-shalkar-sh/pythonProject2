size_list = int(input('Введите размер элементов списка: '))
list_size = input('Введите элементы списка через пробел: ').split()
arr = list(map(int, list_size))
x = int (input('Введите число х: '))
count = 0
for i in range(size_list):
    if arr[i] == x:
        count += 1
print(f'Число {x} встречается в списке "n" {count} раз.')