import binary as binary
import sequential as seq

arr = [1,2,3,4,5,6,7,8,9,10]
isFound = binary.binarySearch(11, arr)
if isFound == True: 
    print("Found")
else:
    print("Not Found")