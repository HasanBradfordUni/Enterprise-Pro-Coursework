class listOperationsManager:
    def __init__(self):
        self.arr = []
        
    def categorise_data(self, arr, categories_type):
        #categorise data into different categories
        if categories_type == "title":
            return "title"
        elif categories_type == "assigned date":
            return "assigned date"
        elif categories_type == "due date":
            return "due date"
        elif categories_type == "status":
            return "status"
        else:
            return "Invalid category type"

    def filter_data(self, arr, filter_type):
        #filter data based on the filter type
        if filter_type == "title":
            return "title"
        elif filter_type == "assigned date":
            return "assigned date"
        elif filter_type == "due date":
            return "due date"
        elif filter_type == "status":
            return "status"
        else:
            return "Invalid filter type"

    #write a binary search (textual) and merge sort function on a list 
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2  # Find the middle index
            if target in arr[mid]:
                return mid  # Target found
            elif arr[mid] < target:
                low = mid + 1  # Focus on the right half
            else:
                high = mid - 1  # Focus on the left half

        return -1  # Target not found

    def merge_sort(self, arr):
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
        return merged
