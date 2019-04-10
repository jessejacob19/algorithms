def selection_sort(arr):
  smallest = arr[0]
  smallest_pos = 0
  for i in range(len(arr)):
    for j in range(i, len(arr)):
      if arr[j] < smallest:
        smallest = arr[j]
        smallest_pos = j
    arr[i], arr[smallest_pos] = arr[smallest_pos], arr[i]
    smallest = arr[i+1]
    smallest_pos = i + 1
  return arr
