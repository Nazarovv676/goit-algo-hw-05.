def binary_search_with_bounds(arr, target):
    """
    Виконує двійковий пошук у відсортованому масиві дробових чисел.
    
    Параметри:
    arr (list): Відсортований масив дробових чисел.
    target (float): Елемент, який потрібно знайти.

    Повертає:
    tuple: (кількість ітерацій, верхня межа).
    """
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None  # Верхня межа

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            # Якщо знайдено точний збіг, верхня межа — це arr[mid].
            return iterations, arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            upper_bound = arr[mid]  # Можливий кандидат на верхню межу
            high = mid - 1

    # Якщо target не знайдено, верхньою межею буде arr[low], якщо low не виходить за межі масиву
    if low < len(arr):
        upper_bound = arr[low]

    return iterations, upper_bound


# Тестування:
sorted_array = [1.1, 2.5, 3.3, 4.4, 5.9, 7.0, 8.6, 10.2]
target_value = 6.0

result = binary_search_with_bounds(sorted_array, target_value)
print(f"Кількість ітерацій: {result[0]}")
print(f"Верхня межа: {result[1]}")