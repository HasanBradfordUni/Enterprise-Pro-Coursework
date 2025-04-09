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
        self.databaseTester.test_connection()
    
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

    def handle_choice(self, menu_type):
        if menu_type == "none":
            self.setMenu("main")
            self.display_menu()
            self.get_choice()
            self.handle_choice("main")
        if menu_type == "main":
            if self.choice == 1:
                self.setMenu("database")
                self.display_menu()
                self.get_choice()
                self.handle_choice("database")
            elif self.choice == 2:
                self.setMenu("list_operations")
                self.display_menu()
                self.get_choice()
                self.handle_choice("list_operations")
            elif self.choice == 3:
                self.test_forms()
            elif self.choice == 4:
                self.test_routes()
            elif self.choice == 5:
                print("Exiting...")
                exit(0)
        if menu_type == "database":
            self.display_menu()
            self.get_choice()
            if self.choice == 1:
                self.databaseTester.test_add_user()
            elif self.choice == 2:
                self.databaseTester.test_add_project()
            elif self.choice == 3:
                self.databaseTester.test_add_task()
            elif self.choice == 4:
                self.databaseTester.test_add_user_into_project
            elif self.choice == 5:
                self.databaseTester.test_add_assigned_task()
            elif self.choice == 6:
                self.databaseTester.test_add_task_update()
            elif self.choice == 7:
                self.databaseTester.test_update_project()
            elif self.choice == 8:
                self.databaseTester.test_update_user()
            elif self.choice == 9:
                self.databaseTester.test_update_task()
            elif self.choice == 10:
                self.databaseTester.test_update_user_in_project()
            elif self.choice == 11:
                self.databaseTester.test_update_assigned_task()
            elif self.choice == 12:
                self.databaseTester.test_delete_user()
            elif self.choice == 13:
                self.databaseTester.test_delete_project()
            elif self.choice == 14:
                self.databaseTester.test_delete_task()
            elif self.choice == 15:
                self.databaseTester.test_delete_project_user()
            elif self.choice == 16:
                self.databaseTester.test_delete_assigned_task()
            elif self.choice == 17:
                self.handle_choice("main")
            else:
                print("Exiting...")
                exit(0)
        if menu_type == "list_operations":
            self.display_menu()
            self.get_choice()
            if self.choice == 1:
                self.listOperationsTester.test_merge_sort()
            elif self.choice == 2:
                self.listOperationsTester.test_binary_search()
            elif self.choice == 3:
                self.listOperationsTester.test_filter_data()
            elif self.choice == 4:
                self.listOperationsTester.test_categorise_data()
            elif self.choice == 5:
                self.handle_choice("main")
            else:
                print("Exiting...")
                exit(0)
            
