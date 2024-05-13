def bSort(array):
    # определяем длину массива
    length = len(array)
    # Внешний цикл, N-i-1 проходов
    for i in range(length):
        # Внутренний цикл, N-i-1 проходов
        for j in range(0,length-i-1):
            # Меняем элементы местами
            if array [j]>array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

my_list = [64,55,37,25,46,90]
print('исходный список: ', my_list)

bSort(my_list)

print('Отсортированный список: ', my_list)

a = [3,4,2,6,5]
print(sorted(a))