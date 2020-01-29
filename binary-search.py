def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while(low <= high):
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid -1
        elif target > arr[mid]:
            low = mid + 1
    
    return -1


arr = [20, 50, 65, 79, 81, 87, 90, 98, 112]

position = binary_search(arr, 50)

if(position == -1):
    print("Item not found in the list...")
else: 
    print("Item found in list at position  : ", position+1)
    