import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)  # DEBUG, CRITICAL


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    # Мы будет часто используем длины списков, поэтому удобно сразу создавать переменные для этого
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Мы проверяем, какое значение с начала каждого списка меньше
            # Если элемент в начале левого списка меньше, добавляем его в отсортированный список
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если элемент в начале правого списка меньше, добавляем его в отсортированный список
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        # Если мы достигли конца левого списка, добавляем элементы из правого списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если мы достигли конца правого списка, добавляем элементы из левого списка
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


def merge_sort(nums):
    # Если список представляет собой один элемент, возвращаем его
    if len(nums) <= 1:
        return nums
    # Используем деление с округленим по наименьшему целому для получения средней точки, индексы должны быть целыми числами
    mid = len(nums) // 2
    # Сортируем и объединяем каждую половину
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    # Объединить отсортированные списки в новый
    return merge(left_list, right_list)

with open('input_c1.txt', 'r') as f:
    lines = f.readlines()
f.close()
n = 0
a_list = []

for k in range(len(lines)):
    # logging.info(lines[k].strip("\n"))
    workstr = lines[k].strip()
    if k == 0:
        nstr = workstr.strip("\n")
        n = int(nstr)
        logging.info("n = {}".format(n))
    if k == 1:
        astr_list = workstr.strip("\n").split(" ", int(n))
        a_list = list(map(int, astr_list))
        logging.info("a_list = {}".format(a_list))

# Проверяем, что все работает

random_list_of_nums = merge_sort(a_list)
# print(random_list_of_nums)
if len(random_list_of_nums) < 3:
    print("yes")
    exit(0)
else:
    result = 'yes'
    dif = random_list_of_nums[1] - random_list_of_nums[0]
    for i in range(2, len(random_list_of_nums)):
        difcur = random_list_of_nums[i] - random_list_of_nums[i-1]
        # print(random_list_of_nums[i-1], random_list_of_nums[i])
        if dif != difcur:
            result = 'no'
            break
    print(result)