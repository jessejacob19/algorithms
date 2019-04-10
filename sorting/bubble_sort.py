#never use this sorting algorithm --its trash
def bubble_sort(arr):
  swapped = True

  while swapped:
    swapped = False
    for i in arr:
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        swapped = True
  return arr
