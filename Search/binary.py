def binarySerch(self, data, arr):    
   isFound = sliceSearch(data, arr, 0, len(arr))
   return isFound

def sliceSearch(self, data, arr, ini, length):
    half = ((ini-length)*-1) / 2
    if arr[half] == data:
        return True
    else:
        isFound = False
        if arr[half] > data:
          isFound =  sliceSearch(data, arr, half, length)
        else:
          isFound =  sliceSearch(data, arr, 0, half)
    return isFound       
            
