# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

#As time complexity must be O(log n) we need to implement the binary search and to implement binary search we can utilize the given "an array sorted in ascending order is rotated at some pivot"
# low = 0
# high = len(arr) - 1
# while (low <= high) : 
#     mid = (low + high) //2
    
#     case 1 : if mid is the target position 
#                  return mid
#     case 2 : if arr[mid] <= arr[high] that means right half array is sorted 
#              - Check whether target lies in between arr[mid] to arr[high] .. target > arr[mid] and target <= arr[high]
#              - if YES low = mid + 1
#              - else high = mid - 1
#     case 3 : if arr[low] <= arr[mid] that means left half is sorted
#             - check whether target lies in between left half target > arr[low] and target < arr[mid]
#             - if YES high = mid -1
#             - else low = mid +1 

def search_circular_arr(arr, target): 
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (low + high) //2

        #case- 1
        if(arr[mid] == target):
            return mid
        #case- 2
        elif(arr[mid] <= arr[high]):
            if target > arr[mid] and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
        elif(arr[mid] >= arr[low]):
            if target >= arr[low] and target < arr[mid]:
                high = mid -1
            else:
                low = mid + 1
    
    return -1

print(search_circular_arr([4,5,6,7,0,1,2], 2))