from test_database import testDatabase
from test_list_operations import testListOperations
from test_forms import *
from test_routes import *

class testsManager:
    def __init__(self):
        self.databaseTester = testDatabase()
        self.listOperationsTester = testListOperations()
        self.menu = {}
        self.choice = 0
        self.databaseTester.thisDatabase.create_connection(os.path.join(os.getcwd(), 'Code/database.db'))
    
    def display_menu(self):
        for key, value in self.menu.items():
            print(f"{key}: {value}")
    
    def get_choice(self):
        try:
            self.choice = int(input("Enter your choice: "))
            if self.choice not in list(self.menu.keys()):
                print("Invalid choice. Please try again.")
                self.get_choice()
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.get_choice()
    
    def setMenu(self, menu_type):
        if menu_type == "main":
            self.menu = {
                1: "Database Tests",
                2: "List Operations Tests",
                3: "Form Tests",
                4: "Route Tests",
                5: "Exit"
            }
        elif menu_type == "database":
            self.menu = {
                1: "Add User",
                2: "Add Project",
                3: "Add Task",
                4: "Add User to Project",
                5: "Add Assigned Task",
                6: "Add Task Update",
                7: "Update Project",
                8: "Update User",
                9: "Update Task",
                10: "Update User in Project",
                11: "Update Assigned Task",
                12: "Delete User",
                13: "Delete Project",
                14: "Delete Task",
                15: "Delete User from Project",
                16: "Delete Assigned Task",
                17: "Go Back",
                18: "Exit"
            }
        elif menu_type == "list_operations":
            self.menu = {
                1: "Merge Sort",
                2: "Binary Search",
                3: "Filter Data",
                4: "Categorise Data",
                5: "Go Back",
                6: "Exit"
            }

    def test_forms(self):
        import pytest
    
        # Specify the path to the test file
        test_file = "Testing/test_forms.py"
    
        print(f"Running tests in {test_file}...")
        # Run the tests in the specified file
        result = pytest.main([test_file, "-v"])  # Add verbose output for debugging
        if result == 0:
            print("All form tests passed.")
        else:
            print(f"Some form tests failed with result code: {result}")

    def test_routes(self):
        import pytest
    
        # Specify the path to the test file
        test_file = "Testing/test_routes.py"
    
        print(f"Running tests in {test_file}...")
        # Run the tests in the specified file
        result = pytest.main([test_file, "-v"])  # Add verbose output for debugging
        if result == 0:
            print("All route tests passed.")
        else:
            print(f"Some route tests failed with result code: {result}")

    def handle_choice(self):
        current_menu = "main"
        while True:
            self.setMenu(current_menu)
            self.display_menu()
            self.get_choice()

            if current_menu == "main":
                if self.choice == 1:
                    current_menu = "database"
                elif self.choice == 2:
                    current_menu = "list_operations"
                elif self.choice == 3:
                    self.test_forms()
                elif self.choice == 4:
                    self.test_routes()
                elif self.choice == 5:
                    print("Exiting...")
                    exit(0)
                else:
                    print("Invalid choice. Please try again.")
                    continue

            elif current_menu == "database":
                if self.choice == 1:
                    print("Testing add user...")
                    result = self.databaseTester.test_add_user()
                    print(result)
                elif self.choice == 2:
                    print("Testing add project...")
                    result = self.databaseTester.test_add_project()
                    print(result)
                elif self.choice == 3:
                    print("Testing add task...")
                    result = self.databaseTester.test_add_task()
                    print(result)
                elif self.choice == 4:
                    print("Testing add user to project...")
                    result = self.databaseTester.test_add_user_into_project()
                    print(result)
                elif self.choice == 5:
                    print("Testing add assigned task...")
                    result = self.databaseTester.test_add_assigned_task()
                    print(result)
                elif self.choice == 6:
                    print("Testing add task update...")
                    result = self.databaseTester.test_add_task_update()
                    print(result)
                elif self.choice == 7:
                    print("Testing update project...")
                    result = self.databaseTester.test_update_project()
                    print(result)
                elif self.choice == 8:
                    print("Testing update user...")
                    result = self.databaseTester.test_update_user()
                    print(result)
                elif self.choice == 9:
                    print("Testing update task...")
                    result = self.databaseTester.test_update_task()
                    print(result)
                elif self.choice == 10:
                    print("Testing update user in project...")
                    result = self.databaseTester.test_update_user_in_project()
                    print(result)
                elif self.choice == 11:
                    print("Testing update assigned task...")
                    result = self.databaseTester.test_update_assigned_task()
                    print(result)
                elif self.choice == 12:
                    print("Testing delete user...")
                    result = self.databaseTester.test_delete_user()
                    print(result)
                elif self.choice == 13:
                    print("Testing delete project...")
                    result = self.databaseTester.test_delete_project()
                    print(result)
                elif self.choice == 14:
                    print("Testing delete task...")
                    result = self.databaseTester.test_delete_task()
                    print(result)
                elif self.choice == 15:
                    print("Testing delete user from project...")
                    result = self.databaseTester.test_delete_project_user()
                    print(result)
                elif self.choice == 16:
                    print("Testing delete assigned task...")
                    result = self.databaseTester.test_delete_assigned_task()
                    print(result)
                elif self.choice == 17:
                    current_menu = "main"
                elif self.choice == 18:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        
            elif current_menu == "list_operations":
                if self.choice == 1:
                    print("Testing merge sort...")
                    result = self.listOperationsTester.test_merge_sort()
                    print(result)
                elif self.choice == 2:
                    print("Testing binary search...")
                    result = self.listOperationsTester.test_binary_search()
                    print(result)
                elif self.choice == 3:
                    print("Testing filter data...")
                    result = self.listOperationsTester.test_filter_data()
                    print(result)
                elif self.choice == 4:
                    print("Testing categorise data...")
                    result = self.listOperationsTester.test_categorise_data()
                    print(result)
                elif self.choice == 5:
                    current_menu = "main"
                elif self.choice == 6:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")
    
    def manage_tests(self):
        print("Welcome to the Test Manager!")
        self.handle_choice()

if __name__ == "__main__":
    test_manager = testsManager()
    test_manager.manage_tests()