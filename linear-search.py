def linear_search(arr, target):
    for i in range(0, len(arr)):
        if(arr[i] == target):
            return i #return index value for the target found in the list 

    return -1 #return -1 if target not found in given list

arr = [2, 4, 90, 18, 22, 6, 110, 5, 3, 4]

position = linear_search(arr, 90)

if(position == -1):
    print("Item not found in the list...")
else: 
    print("Item found in list at position  : ", position+1)


