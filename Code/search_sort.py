class listOperationsManager:
    def __init__(self):
        self.arr = []
        
    def categorise_data(self, arr, categories_type):
        #categorise data into different categories
        if categories_type == "title":
            #write logic to seperate the data by alphabetical order
            categories = []
            #if statements should be used and the alphabetical ranges are as follows:
            #range 1 is 0-9
            #range 2 is A-E
            #range 3 is F-J
            #range 4 is K-O
            #range 5 is P-T
            #range 6 is U-Z
            #create seperate lists for each range and return them as a list of lists
            return categories
        elif categories_type == "assigned date":
            categories = []
            #write logic to seperate the data by assigned date
            #if statements should be used and the assigned dates should be split by every 3 months
            #create seperate lists for each 3 months and return them as a list of lists
            return categories
        elif categories_type == "due date":
            categories = []
            #write logic to seperate the data by due date
            #if statements should be used and the due dates should be split by every 3 months
            #create seperate lists for each 3 months and return them as a list of lists
            return categories
        elif categories_type == "status":
            categories = []
            #write logic to seperate the data by status
            #if statements should be used and the status should be split by the following statuses:
            #In Progress, Complete, New, Overdue, Other
            #create seperate lists for each status and return them as a list of lists
            #some statuses may not be present in the data, include a check for this
            return categories
        elif categories_type == "team":
            categories = []
            #write logic to seperate the data by team
            #if statements should be used and the teams should be split by the following teams:
            #Police, Intern, Other
            #create seperate lists for each team and return them as a list of lists
            return categories
        elif categories_type == "review":
            categories = []
            #write logic to seperate the data by review
            #if statements should be used and the review should be split by the following review times:
            #1 day, 3 days, 1 week, 2 weeks, 1 month
            #create seperate lists for each review time and return them as a list of lists
            return categories
        else:
            categories = "Invalid category type"
        return categories

    def filter_data(self, arr, filter_type):
        #filter data based on the filter type
        if filter_type == "title":
            #write logic to filter the data by title
            #use a for loop to iterate through the data and check if the title contains the filter word
            #return a list of the filtered data
            return filtered_data
        elif filter_type == "assigned date":
            #write logic to filter the data by assigned date
            #use a for loop to iterate through the data and check if the assigned date matches the filter date
            #return a list of the filtered data
            return filtered_data
        elif filter_type == "due date":
            #write logic to filter the data by due date
            #use a for loop to iterate through the data and check if the due date matches the filter date
            #return a list of the filtered data
            return filtered_data
        elif filter_type == "status":
            #write logic to filter the data by status
            #use a for loop to iterate through the data and check if the status matches the filter status
            #return a list of the filtered data
            return filtered_data
        elif filter_type == "team":
            #write logic to filter the data by team
            #use a for loop to iterate through the data and check if the team matches the filter team
            #return a list of the filtered data
            return filtered_data
        elif filter_type == "review":
            #write logic to filter the data by review
            #use a for loop to iterate through the data and check if the review matches the filter review time
            #return a list of the filtered data
            return filtered_data
        else:
            filtered_data = "Invalid filter type"

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
