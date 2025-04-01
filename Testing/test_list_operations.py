import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add project root to path

from Code.search_sort import listOperationsManager

class testListOperations:
    def __init__(self):
        self.listOperationsManager = listOperationsManager()

    def test_categorise_data(self):
        # List of sample tasks
        tasks = [
    [1, "Write report", "Writing a report for the system", "In-progress", "12/03/25", "26/03/25", 1],
    [2, "Review code", "Reviewing code of the system", "Complete", "14/03/25", "21/03/25", 1],
    [3, "Fix bugs", "Fixing bugs in the system", "In-progress", "15/03/25", "24/03/25", 1],
    [4, "Send email", "Sending emails to the stakeholders", "Complete", "16/03/25", "18/03/25", 2],
    [5, "Attend meeting", "Attending a project planning meeting", "Scheduled", "20/03/25", "20/03/25", 2],
    [6, "Plan project", "Defining project scope and deliverables", "Not started", "22/03/25", "30/03/25", 3],
    [7, "Design UI", "Creating the user interface for the system", "In-progress", "25/03/25", "05/04/25", 3]
]

        menu = """1.Sort by titles
        2. Sort by assigned dates
        3. Sort by due dates
        4. Sort by task status"""
        print(menu)
        choice  = int(input("Enter your choice from the menue above: "))

        if choice == 1:
            sorted_tasks = self.listOperationsManager.categorise_data(tasks, 'title')
            if not sorted_tasks:
                print("No sorted tasks - Categorise data test failed")
            else:
                print("Sorted tasks:",sorted_tasks)
                print("Sorted tasks present - Categorise data test sucessful")
        if choice == 2:
            sorted_tasks = self.listOperationsManager.categorise_data(tasks, 'assigned date')
            if not sorted_tasks:
                print("No sorted tasks - Categorise data test failed")
            else:
                print("Sorted tasks:",sorted_tasks)
                print("Sorted tasks present - Categorise data test sucessful")
        if choice == 3:
            sorted_tasks = self.listOperationsManager.categorise_data(tasks, 'due date')
            if not sorted_tasks:
                print("No sorted tasks - Categorise data test failed")
            else:
                print("Sorted tasks:",sorted_tasks)
                print("Sorted tasks present - Categorise data test sucessful")
        if choice == 4:
            sorted_tasks = self.listOperationsManager.categorise_data(tasks, 'status')
            if not sorted_tasks:
                print("No sorted tasks - Categorise data test failed")
            else:
                print("Sorted tasks:",sorted_tasks)
                print("Sorted tasks present - Categorise data test sucessful")
        else:
            print("Wrong choice chosen - Categorise data test failed")

    def test_filter_data(self):
        # List of sample tasks# List of task titles
        tasks = [
    [1, "Write report", "Writing a report for the system", "In-progress", "12/03/25", "26/03/25", 1],
    [2, "Review code", "Reviewing code of the system", "Complete", "14/03/25", "21/03/25", 1],
    [3, "Fix bugs", "Fixing bugs in the system", "In-progress", "15/03/25", "24/03/25", 1],
    [4, "Send email", "Sending emails to the stakeholders", "Complete", "16/03/25", "18/03/25", 2],
    [5, "Attend meeting", "Attending a project planning meeting", "Scheduled", "20/03/25", "20/03/25", 2],
    [6, "Plan project", "Defining project scope and deliverables", "Not started", "22/03/25", "30/03/25", 3],
    [7, "Design UI", "Creating the user interface for the system", "In-progress", "25/03/25", "05/04/25", 3]
]

        menu = """1.Filter by titles
        2. Filter by assigned dates
        3. Filter by due dates
        4. Filter by task status"""
        print(menu)
        choice  = int(input("Enter your choice from the menue above: "))

        if choice == 1:
            filter_tasks = self.listOperationsManager.filter_data(tasks, 'title')
            if not filter_tasks:
                print("No filtered tasks - Filter data test failed")
            else:
                print("Filtered tasks:",filter_tasks)
                print("Filtered tasks present - Filter data test sucessful")
        if choice == 2:
            filter_tasks = self.listOperationsManager.categorise_data(tasks, 'assigned date')
            if not filter_tasks:
                print("No filtered tasks - Filter data test failed")
            else:
                print("Filtered tasks:",filter_tasks)
                print("Filtered tasks present - Filter data test sucessful")
        if choice == 3:
            filter_tasks = self.listOperationsManager.categorise_data(tasks, 'due date')
            if not filter_tasks:
                print("No filtered tasks - Filter data test failed")
            else:
                print("Filtered tasks:",filter_tasks)
                print("Filtered tasks present - Filter data test sucessful")
        if choice == 4:
            filter_tasks = self.listOperationsManager.categorise_data(tasks, 'status')
            if not filter_tasks:
                print("No filtered tasks - Filter data test failed")
            else:
                print("Filtered tasks:",filter_tasks)
                print("Filtered tasks present - Filter data test sucessful")
        else:
            print("Wrong choice chosen - Filter data test failed")
    
        
    def test_binary_search(self):
        # List of task titles
        tasks = [
            "Write report",
            "Review code",
            "Fix bugs",
            "Send email",
            "Attend meeting",
            "Plan project",
            "Design UI"
        ]

        # Sorting the task list (binary search requires sorted data)
        tasks.sort()

        # Task to search for
        target_task = input('Enter the tite of a task to search for: ')

        # Perform binary search
        index = self.listOperationsManager.binary_search(tasks, target_task)

        # Output the result
        if index != -1:
            print(f'Task "{target_task}" found at index {index}.')
        else:
            print(f'Task "{target_task}" not found.')

        try:
            assert index != -1
            return "Binary search test successful"
        except AssertionError:
            return "Binary search test unsuccessful"

    def test_merge_sort(self):
        # List of task titles
        tasks = [
            "Write report",
            "Review code",
            "Fix bugs",
            "Send email",
            "Attend meeting",
            "Plan project",
            "Design UI"
        ]

        sorted_tasks = self.listOperationsManager.merge_sort(tasks)
        print("Sorted tasks:", sorted_tasks)
        tasks.sort()
        
        try:
            assert sorted_tasks == tasks
            return "Merge sort test successful"
        except AssertionError:
            return "Merge sort test unsuccessful"
        
if __name__ == "__main__":
    tester = testListOperations()
    tester.test_categorise_data()
    tester.test_filter_data()
    print(tester.test_binary_search())
    print(tester.test_merge_sort())
