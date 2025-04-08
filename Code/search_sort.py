class listOperationsManager:
    def __init__(self):
        self.arr = []
        
    def categorise_data(self, arr, categories_type):
        #categorise data into different categories
        categories = []
        if categories_type == "title":
            #write logic to seperate the data by alphabetical order
            #if statements should be used and the alphabetical ranges are as follows:
            titles1 = [] #range 1 is 0-9
            titles2 = [] #range 2 is A-E
            titles3 = [] #range 3 is F-J
            titles4 = [] #range 4 is K-O
            titles5 = [] #range 5 is P-T
            titles6 = [] #range 6 is U-Z
            #create seperate lists for each range and return them as a list of lists
            for task in arr:
                if 47 < ord(task[1][0]) < 58:
                    titles1.append(task)
                elif 64 < ord(task[1][0]) < 70:
                    titles2.append(task)
                elif 69 < ord(task[1][0]) < 75:
                    titles3.append(task)
                elif 74 < ord(task[1][0]) < 80:
                    titles4.append(task)
                elif 79 < ord(task[1][0]) < 85:
                    titles5.append(task)
                else:
                    titles6.append(task)
            categories.append(titles1)
            categories.append(titles2)
            categories.append(titles3)
            categories.append(titles4)
            categories.append(titles5)
            categories.append(titles6)
            return categories
        elif categories_type == "assigned date":
            for task in arr:
                if 
            #write logic to seperate the data by assigned date
            #if statements should be used and the assigned dates should be split by every 3 months
            #create seperate lists for each 3 months and return them as a list of lists
            return categories
        elif categories_type == "due date":
            #write logic to seperate the data by due date
            #if statements should be used and the due dates should be split by every 3 months
            #create seperate lists for each 3 months and return them as a list of lists
            return categories
        elif categories_type == "status":
            #write logic to seperate the data by status
            #if statements should be used and the status should be split by the following statuses:
            #In Progress, Complete, New, Overdue, Other
            in_progress = [] #range 1 is In Progress
            complete = [] #range 2 is Complete
            new = [] #range 3 is New
            overdue = [] #range 4 is Overdue
            other = [] #range 5 is Other
            #create seperate lists for each status and return them as a list of lists
            for task in arr:
                if task[3] == "In progress":
                    in_progress.append(task)
                elif task[3] == "Complete":
                    complete.append(task)
                elif task[3] == "New":
                    new.append(task)
                elif task[3] == "Overdue":
                    overdue.append(task)
                else:
                    other.append(task)
            categories.append(in_progress)
            categories.append(complete)
            categories.append(new)
            categories.append(overdue)        
            categories.append(other)
            #some statuses may not be present in the data, include a check for this
            return categories
        elif categories_type == "team":
            #write logic to seperate the data by team
            #if statements should be used and the teams should be split by the following teams:
            #Police, Intern, Other
            police = [] #range 1 is Police
            intern = [] #range 2 is Intern
            other = [] #range 3 is Other
            #create seperate lists for each team and return them as a list of lists
            for project in arr:
                if project[4] == "Police":
                    police.append(project)
                elif project[4] == "Intern":
                    intern.append(project)
                else:
                    other.append(project)
            categories.append(police)
            categories.append(intern)
            categories.append(other)
            return categories
        elif categories_type == "review":
            #write logic to seperate the data by review
            #if statements should be used and the review should be split by the following review times:
            #1 day, 3 days, 1 week, 2 weeks, 1 month
            review1 = [] #range 1 is 1 day
            review2 = [] #range 2 is 3 days
            review3 = [] #range 3 is 1 week
            review4 = [] #range 4 is 2 weeks
            review5 = [] #range 5 is 1 month
            #create seperate lists for each review time and return them as a list of lists
            for project in arr:
                if project[3] == "1 day":
                    review1.append(project)
                elif project[3] == "3 days":
                    review2.append(project)
                elif project[3] == "1 week":
                    review3.append(project)
                elif project[3] == "2 weeks":
                    review4.append(project)
                else:
                    review5.append(project)
            categories.append(review1)
            categories.append(review2)
            categories.append(review3)
            categories.append(review4)
            categories.append(review5)
            return categories
        else:
            categories = "Invalid category type"
        return categories

    def filter_data(self, arr, filter_type, filter_word):
        #filter data based on the filter type
        filtered_data = []
        if filter_type == "assigned date":
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
            for task in arr:
                if task[3] == filter_word:
                    filtered_data.append(task)
            #return a list of the filtered data
            return filtered_data
        elif filter_type == "team":
            #write logic to filter the data by team
            #use a for loop to iterate through the data and check if the team matches the filter team
            for project in arr:
                if project[4] == filter_word:
                    filtered_data.append(project)
            #return a list of the filtered data
            return filtered_data
        elif filter_type == "review":
            #write logic to filter the data by review
            #use a for loop to iterate through the data and check if the review matches the filter review time
            for project in arr:
                if project[3] == filter_word:
                    filtered_data.append(project)
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
