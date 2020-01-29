# searching-problems
- Searching is the process of finding a given value position in a list of values.
- It decides whether a search key is present in the data or not.
- It is the algorithmic process of finding a particular item in a collection of items.
- It can be done on internal data structure or on external data structure.

## Mainly two techniques available fot Searching
1. Sequential Search (Linear Search)
2. Binary Search

# 1. Linear Search
- It is an basic and simple search algorithm -- applied to search target item when the given list is an unsorted list. 
- Target element is compared sequentially with each element of a collection until it is found. Otherwise it will traverse through that list until it reaches to the end of the list.

## Time and Space Complexity :
- Best Time Complexity: O(1)
- Average Time Complexity: O(n)
- Worst Time Complexity:  O(n)
- Best Space Complexity: O(1)

# 2. Binary Search
- Binary Search is used for searching an element in a sorted array.
- It is a fast search algorithm with run-time complexity of O(log n).
- Binary search works on the principle of divide and conquer.
- This searching technique looks for a particular element by comparing the middle most element of the collection.
- It is useful when there are large number of elements in an array.

- Binary searching starts with middle element. If the element is equal to the element that we are searching then return true. If the element is less than then move to the right of the list or if the element is greater than then move to the left of the list. Repeat this, till you find an element.



