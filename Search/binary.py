def binarySearch(data, arr):    
   isFound = sliceSearch(data, arr, 0, len(arr))
   return isFound

def sliceSearch(data, arr, ini, length):
    if ini >= length:
        return False
    half = ((length+ini)) / 2
    half_index = int(half)
    if arr[half_index] == data:
        return True
    else:
        isFound = False
        if arr[half_index] > data:
            isFound =  sliceSearch(data, arr, 0, half_index-1)
        else:
            isFound =  sliceSearch(data, arr, half_index+1, length)
          
    return isFound       
            
