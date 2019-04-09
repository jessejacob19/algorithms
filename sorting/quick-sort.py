def quick_sort(arr, low, high):
  if low < high:
    partition_index = partition(arr, low, high)

    quick_sort(arr, low, partition_index - 1)
    quick_sort(arr, partition_index + 1, high)
  return arr


def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1

  for j in range(low, high):
    if j <= pivot:
      i+=1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[high] = arr[high], arr[i + 1]

  return i + 1





arr = [1,23,4,66,3,2,5,7,8,33,22]
# low is starting index, high is end index
print(quick_sort(arr, 0, len(arr)-1))