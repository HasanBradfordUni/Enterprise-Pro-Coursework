"""listOperationsManager(); binary_search(arr: list, target: string); 
categorise_data(arr: list, categories_type: string); 
merge_sort(arr: list); filter_data(arr: list, filter_type: string);"""

class listOperationsManager:
    def __init__(self):
        

#write a binary search (textual) and merge sort function on a list 
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Focus on the right half
        else:
            high = mid - 1  # Focus on the left half

    return -1  # Target not found

sorted_list = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
target = 23

result = binary_search(sorted_list, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")


def merge_sort(arr):
    width = 1
    n = len(arr)

    while width < n:
        left = 0
        while left < n:
            mid = min(left + width, n)
            right = min(left + 2 * width, n)
            # Merge two halves
            merged = []
            i, j = left, mid
            while i < mid and j < right:
                if arr[i] < arr[j]:
                    merged.append(arr[i])
                    i += 1
                else:
                    merged.append(arr[j])
                    j += 1
            # Add the leftovers
            merged.extend(arr[i:mid])
            merged.extend(arr[j:right])
            # Replace in the original array
            arr[left:right] = merged
            left += 2 * width
        width *= 2
