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

  #     BinarySearch(A[0..N-1], value) {
  #     low = 0
  #     high = N - 1
  #     while (low <= high) {
  #         // invariants: value > A[i] for all i < low
  #                        value < A[i] for all i > high
  #         mid = (low + high) / 2
  #         if (A[mid] > value)
  #             high = mid - 1
  #         else if (A[mid] < value)
  #             low = mid + 1
  #         else
  #             return mid
  #     }
  #     return not_found // value would be inserted at index "low"
  # }

  def binary_Search(arr, value):
    low = 0
    high = len(arr) - 1
    while low <= high:
      mid = math.floor((low + high)/2)
      if arr[mid] > value:
        high = mid - 1
      elif arr[mid] < value:
        low = mid + 1
      else:
        return mid
    return None