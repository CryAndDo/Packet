import random

def generate_random_numbers_and_find_sum(file_path, n):

    numbers = [random.uniform(-100, 100) for _ in range(n)]

    with open(file_path, 'w') as file:
        for num in numbers:
            file.write(f'{num:.6f}\n')

    min_num = float('inf')
    max_num = float('-inf')

    with open(file_path, 'r') as file:
        for line in file:
            num = float(line.strip())
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num

    sum_min_max = min_num + max_num
    print(f"Сумма минимального ({min_num}) и максимального ({max_num}) элементов равна {sum_min_max}")

    return sum_min_max

from mypackage.module1 import generate_random_numbers_and_find_sum

file_path = 'numbers.txt'
n = 10

generate_random_numbers_and_find_sum(file_path, n)

