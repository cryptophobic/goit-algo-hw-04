import timeit
import random


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
	# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Реалізація Timsort (вбудованого алгоритму в Python)
def timsort(arr):
    return sorted(arr)

# Генерація тестових наборів даних
def generate_data(n):
    return random.sample(range(n), n), list(range(n)), list(range(n, 0, -1))

# Функція для вимірювання часу виконання
def measure_time(sort_func, arr):
    return timeit.timeit(lambda: sort_func(arr.copy()), number=1)

# Тестування
sizes = [1000, 5000, 10000]
for size in sizes:
    random_data, sorted_data, reversed_data = generate_data(size)

    print(f"\nData size: {size}")

    # Випадкові дані
    print(f"Random data:")
    print(f"Insertion Sort: {measure_time(insertion_sort, random_data):.6f} seconds")
    print(f"Merge Sort: {measure_time(merge_sort, random_data):.6f} seconds")
    print(f"Timsort: {measure_time(timsort, random_data):.6f} seconds")

    # Відсортовані дані
    print(f"Sorted data:")
    print(f"Insertion Sort: {measure_time(insertion_sort, sorted_data):.6f} seconds")
    print(f"Merge Sort: {measure_time(merge_sort, sorted_data):.6f} seconds")
    print(f"Timsort: {measure_time(timsort, sorted_data):.6f} seconds")

    # Реверсні дані
    print(f"Reversed data:")
    print(f"Insertion Sort: {measure_time(insertion_sort, reversed_data):.6f} seconds")
    print(f"Merge Sort: {measure_time(merge_sort, reversed_data):.6f} seconds")
    print(f"Timsort: {measure_time(timsort, reversed_data):.6f} seconds")
