import hashlib
import json
import os

# Utility function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Utility function to load user data from a file
def load_user_data():
    if not os.path.exists("users.json"):
        return {}
    with open("users.json", "r") as file:
        return json.load(file)

# Utility function to save user data to a file
def save_user_data(data):
    with open("users.json", "w") as file:
        json.dump(data, file)

# User Registration
def register_user():
    users = load_user_data()
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Please try again.")
        return False
    password = input("Enter a password: ")
    hashed_password = hash_password(password)
    users[username] = {"password": hashed_password, "tasks": []}
    save_user_data(users)
    print("Registration successful!")
    return True

# User Login
def login_user():
    users = load_user_data()
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found.")
        return None
    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    if users[username]["password"] == hashed_password:
        print("Login successful!")
        return username
    else:
        print("Incorrect password.")
        return None

# Add a Task
def add_task(username):
    users = load_user_data()
    task_description = input("Enter the task description: ")
    task_id = len(users[username]["tasks"]) + 1
    task = {"id": task_id, "description": task_description, "status": "Pending"}
    users[username]["tasks"].append(task)
    save_user_data(users)
    print("Task added successfully!")

# View Tasks
def view_tasks(username):
    users = load_user_data()
    tasks = users[username]["tasks"]
    if tasks:
        for task in tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    else:
        print("No tasks found.")

# Mark a Task as Completed
def mark_task_completed(username):
    users = load_user_data()
    task_id = int(input("Enter the task ID to mark as completed: "))
    for task in users[username]["tasks"]:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_user_data(users)
            print("Task marked as completed!")
            return
    print("Task not found.")

# Delete a Task
def delete_task(username):
    users = load_user_data()
    task_id = int(input("Enter the task ID to delete: "))
    tasks = users[username]["tasks"]
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            save_user_data(users)
            print("Task deleted successfully!")
            return
    print("Task not found.")

# Main Menu
def main_menu(username):
    while True:
        print("\nTask Manager Menu")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark a Task as Completed")
        print("4. Delete a Task")
        print("5. Logout")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            mark_task_completed(username)
        elif choice == "4":
            delete_task(username)
        elif choice == "5":
            print("Logging out")
            break
        else:
            print("Invalid option. Please try again.")

# Main Program Loop
def main():
    while True:
        print("\nWelcome to the Task Manager")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            register_user()
        elif choice == "2":
            username = login_user()
            if username:
                main_menu(username)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
