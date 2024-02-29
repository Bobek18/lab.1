def find_k_largest(array, k):
    if not 1 <= k <= len(array):
        raise ValueError("k має бути в діапазоні від 1 до len(array)")
    k_largest_element, pivot_index = quickselect(array, k - 1)
    return k_largest_element, pivot_index
def quickselect(array, k):
    if len(array) == 1:
        return array[0], 0
    pivot = array[-1]
    smaller, larger = partition(array, pivot)
    if k < len(smaller):
        return quickselect(smaller, k)
    elif k == len(smaller):
        return pivot, len(smaller)
    else:
        return quickselect(larger, k - len(smaller) - 1)
def partition(array, pivot):
    smaller = []
    larger = []

    for element in array:
        if element < pivot:
            smaller.append(element)
        else:
            larger.append(element)

    return smaller, larger
array = [15, 7, 22, 9, 36, 2, 42, 18]
k = 3

k_largest_element, index = find_k_largest(array, k)

print(f"Знайдений {k} найбільший елемент: {k_largest_element}")
print(f"Позиція {k} найбільшого елемента в масиві: {index}")