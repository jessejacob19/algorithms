def linear_search(arr, value):
  #searches every element in the list linearly and if
  #the result is found it returns the first position that matches it
  # otherwise it returns None
  for i in arr:
    if arr[i] == value:
      return i
  return None


def linear_search_multiple(arr, value):
  #returns a list of positions where the value matches item in the array
  pos_list = []
  for i in arr:
    if arr[i] == value:
      pos_list.append(i)
  return pos_list