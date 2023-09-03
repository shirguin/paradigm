# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.

def bin_search(arr, num):
    left = 0
    right = len(arr)-1
    index = 0
    res = -1

    while left <= right:
        index = (left + right) // 2

        if arr[index] == num:
            res = index
            break

        if arr[index] < num:
            left = index + 1
        else:
            right = index - 1

    return res


arr_1 = [1, 2, 7, 9, 10, 13, 18, 26, 45, 56, 71, 85]

print(bin_search(arr_1, 10))
print(bin_search(arr_1, 56))
print(bin_search(arr_1, -10))
print(bin_search(arr_1, 99))
