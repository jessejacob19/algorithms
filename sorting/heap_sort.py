def heap_sort(arr):
  n = len(arr)
  build_heap(arr)

  for i in range(n -1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, n, i)
  

def build_heap(arr):
  # build a maxheap
  n = len(arr)
  for i in range(n, -1, -1):
    heapify(arr, n, i)1

def heapify(arr, n, i):
  largest = i #initialise largest as root
  l = 2 * i + 1
  r = 2 * i + 2

  #see if left child of root existsand is greater than root
  if r < n and arr[largest] < arr[r]:
    largest = r

  # change root, if needed
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    #heapify the root
    heapify(arr, n, largest)