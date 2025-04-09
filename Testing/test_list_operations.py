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
            [5, "Attend meeting", "Attending a project planning meeting", "New", "20/03/25", "20/03/25", 2],
            [6, "Plan project", "Defining project scope and deliverables", "New", "22/03/25", "30/03/25", 3],
            [7, "Design UI", "Creating the user interface for the system", "In-progress", "25/03/25", "05/04/25", 3]
        ]

        # List of sample projects
        projects = [
            [1, "A Project", "Details of Project A", "In-progress", "3 days", "Owner A"],
            [2, "Project B", "Details of Project B", "Complete", "1 week", "Owner B"],
            [3, "012 Project", "Details of Project 012", "In-progress", "2 weeks", "Owner C"],
            [4, "Project D", "Details of Project D", "Complete", "1 month", "Owner D"],
            [5, "Finding a new project", "Details of Project F", "In-progress", "3 days", "Owner E"],
            [6, "King Project", "Details of Project King", "Complete", "1 week", "Owner F"],
            [7, "USA Project", "Details of Project USA", "In-progress", "2 weeks", "Owner G"]
        ]

        menu = """1. Sort by titles
2. Sort by assigned dates
3. Sort by due dates
4. Sort by task status
5. Sort by project status
6. Sort by project review dates
7. Sort by project titles"""
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
        if choice == 5:
            sorted_projects = self.listOperationsManager.categorise_data(projects, 'status')
            if not sorted_projects:
                print("No sorted projects - Categorise data test failed")
            else:
                print("Sorted projects:",sorted_projects)
                print("Sorted projects present - Categorise data test sucessful")
        if choice == 6:
            sorted_projects = self.listOperationsManager.categorise_data(projects, 'review')
            if not sorted_projects:
                print("No sorted projects - Categorise data test failed")
            else:
                print("Sorted projects:",sorted_projects)
                print("Sorted projects present - Categorise data test sucessful")
        if choice == 7:
            sorted_projects = self.listOperationsManager.categorise_data(projects, 'title')
            if not sorted_projects:
                print("No sorted projects - Categorise data test failed")
            else:
                print("Sorted projects:",sorted_projects)
                print("Sorted projects present - Categorise data test sucessful")
        else:
            print("Wrong choice chosen - Categorise data test failed")

    def test_filter_data(self):
        # List of sample tasks
        tasks = [
            [1, "Write report", "Writing a report for the system", "In-progress", "12/03/25", "26/03/25", 1],
            [2, "Review code", "Reviewing code of the system", "Complete", "14/03/25", "21/03/25", 1],
            [3, "Fix bugs", "Fixing bugs in the system", "In-progress", "15/03/25", "24/03/25", 1],
            [4, "Send email", "Sending emails to the stakeholders", "Complete", "16/03/25", "18/03/25", 2],
            [5, "Attend meeting", "Attending a project planning meeting", "New", "20/03/25", "20/03/25", 2],
            [6, "Plan project", "Defining project scope and deliverables", "New", "22/03/25", "30/03/25", 3],
            [7, "Design UI", "Creating the user interface for the system", "In-progress", "25/03/25", "05/04/25", 3]
        ]

        # List of sample projects
        projects = [
            [1, "Project A", "Details of Project A", "In-progress", "3 days", "Owner A"],
            [2, "Project B", "Details of Project B", "Complete", "1 week", "Owner B"],
            [3, "Project C", "Details of Project C", "In-progress", "2 weeks", "Owner C"],
            [4, "Project D", "Details of Project D", "Complete", "1 month", "Owner D"],
            [5, "Project E", "Details of Project E", "In-progress", "3 days", "Owner E"],
            [6, "Project F", "Details of Project F", "Complete", "1 week", "Owner F"],
            [7, "Project G", "Details of Project G", "In-progress", "2 weeks", "Owner G"]
        ]

        menu = """1. Filter by 'New' tasks (status)
2. Filter by 'In-progress' tasks (status)
3. Filter by 'Complete' tasks (status)
4. Filter by 'Overdue' tasks (status)
5. Filter by 'In-progress' projects (status)
6. Filter by 'Complete' projects (status)
7. Filter by '1 day' projects (review)
8. Filter by '3 days' projects (review)
9. Filter by '1 week' projects (review)
10. Filter by '2 weeks' projects (review)
11. Filter by '1 month' projects (review)"""
        print(menu)
        choice  = int(input("Enter your choice from the menue above: "))

        if choice == 1:
            filter_tasks = self.listOperationsManager.filter_data(tasks, 'status', 'New')
            if not filter_tasks:
                print("No filtered tasks - Filter data test failed")
            else:
                print("Filtered tasks:",filter_tasks)
                print("Filtered tasks present - Filter data test sucessful")
        if choice == 2:
            filter_tasks = self.listOperationsManager.categorise_data(tasks, 'status', 'In-progress')
            if not filter_tasks:
                print("No filtered tasks - Filter data test failed")
            else:
                print("Filtered tasks:",filter_tasks)
                print("Filtered tasks present - Filter data test sucessful")
        if choice == 3:
            filter_tasks = self.listOperationsManager.categorise_data(tasks, 'status', 'Complete')
            if not filter_tasks:
                print("No filtered tasks - Filter data test failed")
            else:
                print("Filtered tasks:",filter_tasks)
                print("Filtered tasks present - Filter data test sucessful")
        if choice == 4:
            filter_tasks = self.listOperationsManager.categorise_data(tasks, 'status', 'Overdue')
            if not filter_tasks:
                print("No filtered tasks - Filter data test failed")
            else:
                print("Filtered tasks:",filter_tasks)
                print("Filtered tasks present - Filter data test sucessful")
        if choice == 5:
            filter_projects = self.listOperationsManager.categorise_data(projects, 'status', 'In-progress')
            if not filter_projects:
                print("No filtered projects - Filter data test failed")
            else:
                print("Filtered projects:",filter_projects)
                print("Filtered projects present - Filter data test sucessful")
        if choice == 6:
            filter_projects = self.listOperationsManager.categorise_data(projects, 'status', 'Complete')
            if not filter_projects:
                print("No filtered projects - Filter data test failed")
            else:
                print("Filtered projects:",filter_projects)
                print("Filtered projects present - Filter data test sucessful")
        if choice == 7:
            filter_projects = self.listOperationsManager.categorise_data(projects, 'review', '1 day')
            if not filter_projects:
                print("No filtered projects - Filter data test failed")
            else:
                print("Filtered projects:",filter_projects)
                print("Filtered projects present - Filter data test sucessful")
        if choice == 8:
            filter_projects = self.listOperationsManager.categorise_data(projects, 'review', '3 days')
            if not filter_projects:
                print("No filtered projects - Filter data test failed")
            else:
                print("Filtered projects:",filter_projects)
                print("Filtered projects present - Filter data test sucessful")
        if choice == 9:
            filter_projects = self.listOperationsManager.categorise_data(projects, 'review', '1 week')
            if not filter_projects:
                print("No filtered projects - Filter data test failed")
            else:
                print("Filtered projects:",filter_projects)
                print("Filtered projects present - Filter data test sucessful")
        if choice == 10:
            filter_projects = self.listOperationsManager.categorise_data(projects, 'review', '2 weeks')
            if not filter_projects:
                print("No filtered projects - Filter data test failed")
            else:
                print("Filtered projects:",filter_projects)
                print("Filtered projects present - Filter data test sucessful")
        if choice == 11:
            filter_projects = self.listOperationsManager.categorise_data(projects, 'review', '1 month')
            if not filter_projects:
                print("No filtered projects - Filter data test failed")
            else:
                print("Filtered projects:",filter_projects)
                print("Filtered projects present - Filter data test sucessful")
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
    print(tester.test_categorise_data())
    print(tester.test_filter_data())
    print(tester.test_binary_search())
    print(tester.test_merge_sort())
