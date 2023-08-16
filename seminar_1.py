# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):
    n = 1
    while n < len(numbers):
        for i in range(len(numbers) - n):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        n += 1

    return numbers

# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле


def sort_list_declarative(numbers):
    numbers.sort()
    return numbers


arr_1 = [9, 0, -3, 5, 6, 1, 4]
arr_2 = [-10, 9, 0, -3, 5, 6, 1, 4]

print(sort_list_imperative(arr_1))
print(sort_list_declarative(arr_2))
