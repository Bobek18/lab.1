def find_k_largest(array, k):
  if k <= 0 or k > len(array):
    raise ValueError("Невірне значення k: " + str(k))
  _quicksort(array, 0, len(array) - 1)

  return array[len(array) - k], len(array) - k
def _quicksort(array, low, high):
  if low < high:
    pivot_index = _partition(array, low, high)
    _quicksort(array, low, pivot_index - 1)
    _quicksort(array, pivot_index + 1, high)
def _partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]
  array[i + 1], array[high] = array[high], array[i + 1]
  return i + 1
array = [15, 7, 22, 9, 36, 2, 42, 18]
k = 3

k_largest, position = find_k_largest(array, k)

print(f"Знайдений {k} найбільший елемент: {k_largest}")
print(f"Позиція {k} найбільшого елемента в масиві: {position}")
