#Find the Rotation Count in Rotated Sorted array


def count_rotation(arr):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (low + high) // 2
        if(arr[mid - 1] > arr[mid] and arr[mid] < arr[mid + 1]):
            return mid
        elif arr[mid] < arr[high]:
            high = mid - 1
        else:
            low = mid + 1
    
arr = [9, 10, 11, 12, 15, 16, 17, 20, 45, 78, 89, 1, 2, 3, 4, 8]
print("The array rotated by " , count_rotation(arr), " rotations.")