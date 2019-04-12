# binary search goes through an ordered list and halves
# the list size and narrows down where the value is
import math
def binary_search_recursive(arr, value, low, high):
  if high < low:
    retrun None
  mid = math.floor((low + high)/2)
  if arr[mid] > value:
    return binary_search_recursive(arr, value, low, mid - 1)
  elif arr[mid] < value:
    return binary_search_recursive(arr, value, mid + 1, high)
  else:
    return mid