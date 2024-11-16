# Task-Manager
The Problem Statement required us to build a system wherein we have to build a personalised task manager system for a user with a registration and login interface. This allows the user to choose their own username and password.
Coming to the task manager itself, it allows us to store multiple tasks. These are automatically stored in pending status. This can be moved to completed manually. There is also the functionality of just viewing and deleting tasks.

User Registration and Login:

    register_user(): Prompts the user for a username and password. Hashes the password before storing it. Hashlib as been imported for this
    login_user(): Validates the entered credentials against the stored data.

Loading and saving user data
The code stores user and task data in a JSON file
I have used a JSON file as it allows me to store values in the form of a pair (key, value)

Task Management:

    add_task(): Prompts for a task description, assigns a unique ID, and saves it with a "Pending" status.
    view_tasks(): Displays all tasks for the logged-in user.
    mark_task_completed(): Allows a task to be marked as "Completed."
    delete_task(): Deletes a specified task by its ID.

Menu System:

    main_menu(): Displays the interactive menu for the user, allowing them to perform task-related actions until they choose to log out.
    main(): The entry point where users can register, log in, or exit.

