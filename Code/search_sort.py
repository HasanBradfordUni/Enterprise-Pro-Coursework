from datetime import datetime

#This class is used to manage the list operations such as sorting, filtering and categorising data
class listOperationsManager:
    def __init__(self):
        self.arr = []
        
    def categorise_data(self, arr, categories_type):
        #Categorise data into different categories
        categories = []
        if categories_type == "title":
            #Logic to seperate the data by alphabetical order
            titles1 = [] #range 1 is 0-9
            titles2 = [] #range 2 is A-E
            titles3 = [] #range 3 is F-J
            titles4 = [] #range 4 is K-O
            titles5 = [] #range 5 is P-T
            titles6 = [] #range 6 is U-Z

            #Uses the ord() function to get the ASCII value of the first character of the title along
            #with a for loop to iterate through the data and then if statements for categorisation
            for task in arr:
                if 47 < ord(task[1][0]) < 58: #if the ASCII value is between 48 and 57 (0-9), append to titles1
                    titles1.append(task)
                elif 64 < ord(task[1][0]) < 70: #if the ASCII value is between 65 and 70 (A-E), append to titles2
                    titles2.append(task)
                elif 69 < ord(task[1][0]) < 75: #if the ASCII value is between 70 and 75 (F-J), append to titles3
                    titles3.append(task)
                elif 74 < ord(task[1][0]) < 80: #if the ASCII value is between 75 and 80 (K-O), append to titles4
                    titles4.append(task)
                elif 79 < ord(task[1][0]) < 85: #if the ASCII value is between 80 and 85 (P-T), append to titles5
                    titles5.append(task)
                else: #otherwise, append to titles6 (U-Z)
                    titles6.append(task)
            
            #Add the categorised lists to the categories list (list of lists to be returned)
            categories.append(titles1)
            categories.append(titles2)
            categories.append(titles3)
            categories.append(titles4)
            categories.append(titles5)
            categories.append(titles6)
            #Return the list of lists
            return categories
        elif categories_type == "assigned date":
            #Logic to separate the data by assigned date

            #Defines the 3-month intervals
            q1 = [] #range 1 is January - March (first quarter of year)
            q2 = [] #range 2 is April - June (second quarter of year)
            q3 = [] #range 3 is July - September (third quarter of year)
            q4 = [] #range 4 is October - December (fourth quarter of year)

            #Uses the datetime module to parse and categorise dates into 3-month intervals along
            #with a for loop to iterate through the data and then if statements for actual categorisation
            for task in arr: 
                try:
                    #Parse the assigned date (assuming it's in the format 'DD-MM-YYYY')
                    assigned_date = datetime.strptime(task[4], '%d-%m-%Y')
                    #Extract the month from the assigned date
                    month = assigned_date.month

                    #Categorise based on the month
                    if 1 <= month <= 3: #if the month is between January and March, append to q1
                        q1.append(task)
                    elif 4 <= month <= 6: #if the month is between April and June, append to q2
                        q2.append(task)
                    elif 7 <= month <= 9: #if the month is between July and September, append to q3
                        q3.append(task)
                    elif 10 <= month <= 12: #if the month is between October and December, append to q4
                        q4.append(task)
                except ValueError:
                    #Skip over invalid date formats or other errors
                    continue

            #Add the categorised lists to the categories list (list of lists to be returned)
            categories.append(q1)
            categories.append(q2)
            categories.append(q3)
            categories.append(q4)     
            #Return the list of lists        
            return categories
        elif categories_type == "due date":
            #Logic to seperate the data by due date

            #Defines the 3-month intervals
            q1 = [] #range 1 is January - March (first quarter of year)
            q2 = [] #range 2 is April - June (second quarter of year)
            q3 = [] #range 3 is July - September (third quarter of year)
            q4 = [] #range 4 is October - December (fourth quarter of year)

            #Uses the datetime module to parse and categorise dates into 3-month intervals along
            #with a for loop to iterate through the data and then if statements for actual categorisation
            for task in arr:
                try:
                    #Parse the due date (assuming it's in the format 'DD-MM-YYYY')
                    due_date = datetime.strptime(task[5], '%d-%m-%Y')
                    #Extract the month from the due date
                    month = due_date.month

                    #Categorise based on the month
                    if 1 <= month <= 3: #if the month is between January and March, append to q1
                        q1.append(task)
                    elif 4 <= month <= 6: #if the month is between April and June, append to q2
                        q2.append(task)
                    elif 7 <= month <= 9: #if the month is between July and September, append to q3
                        q3.append(task)
                    elif 10 <= month <= 12: #if the month is between October and December, append to q4
                        q4.append(task)
                except ValueError:
                    #Skip over invalid date formats or other errors
                    continue
            
            #Add the categorised lists to the categories list (list of lists to be returned)
            categories.append(q1)
            categories.append(q2)
            categories.append(q3)
            categories.append(q4)
            #Return the list of lists
            return categories
        elif categories_type == "status":
            #Logic to seperate the data by status
            in_progress = [] #range 1 is In Progress
            complete = [] #range 2 is Complete
            new = [] #range 3 is New
            overdue = [] #range 4 is Overdue
            other = [] #range 5 is Other
            #Uses a for loop to iterate through the data and then if statements for categorisation
            for task in arr:
                if task[3] == "In progress": #if the status is In Progress, append to in_progress
                    in_progress.append(task)
                elif task[3] == "Complete": #if the status is Complete, append to complete
                    complete.append(task)
                elif task[3] == "New": #if the status is New, append to new
                    new.append(task)
                elif task[3] == "Overdue": #if the status is Overdue, append to overdue
                    overdue.append(task)
                else: #otherwise, append to other
                    other.append(task)
            #Add the categorised lists to the categories list (list of lists to be returned)
            categories.append(in_progress)
            categories.append(complete)
            categories.append(new)
            categories.append(overdue)        
            categories.append(other)
            #Return the list of lists
            return categories
        elif categories_type == "review":
            #Logic to seperate the data by review
            review1 = [] #range 1 is 1 day
            review2 = [] #range 2 is 3 days
            review3 = [] #range 3 is 1 week
            review4 = [] #range 4 is 2 weeks
            review5 = [] #range 5 is 1 month
            #Uses a for loop to iterate through the data and then if statements for categorisation
            for project in arr:
                if project[3] == "1 day": #if the review time is 1 day, append to review1
                    review1.append(project)
                elif project[3] == "3 days": #if the review time is 3 days, append to review2
                    review2.append(project)
                elif project[3] == "1 week": #if the review time is 1 week, append to review3
                    review3.append(project)
                elif project[3] == "2 weeks": #if the review time is 2 weeks, append to review4
                    review4.append(project)
                else: #otherwise, append to review5
                    review5.append(project)
            #Add the categorised lists to the categories list (list of lists to be returned)
            categories.append(review1)
            categories.append(review2)
            categories.append(review3)
            categories.append(review4)
            categories.append(review5)
            #Return the list of lists
            return categories
        else:
            #If the category type is invalid, append an error message to the categories list
            thisList = ["Invalid category type"]
            categories.append(thisList)
            #Return the list of lists
            return categories

    def filter_data(self, arr, filter_type, filter_word):
        #Filtering data based on the filter type
        filtered_data = []
        if filter_type == "status":
            #Logic to filter the data by status
            #Uses a for loop to iterate through the data and check if the status matches the filter status
            for task in arr:
                if task[3] == filter_word:
                    filtered_data.append(task)
            #Returns a list of the filtered data
            return filtered_data
        elif filter_type == "review":
            #Logic to filter the data by review
            #Uses a for loop to iterate through the data and check if the review matches the filter review time
            for project in arr:
                if project[3] == filter_word:
                    filtered_data.append(project)
            #Returns a list of the filtered data
            return filtered_data
        else:
            filtered_data = "Invalid filter type"

    #Binary search (textual) to find the index of a task in the list
    #Assumes the list is sorted in alphabetical order 
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

    #Merge sort function on a list (non-recursive)
    #This function sorts the list in alphabetical order
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
