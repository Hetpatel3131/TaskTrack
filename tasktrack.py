"""A command-line task manager created for CPS 310.

Author: Het Patel
Course: CPS 310
"""

TASKS_FILE = "tasks.txt"


def display_menu():
    """Display the available TaskTrack menu options."""
    print("\nTaskTrack Menu Updated")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")


def load_tasks(filename):
    """Load tasks from a text file and return them as a list."""
    tasks = []

    try:
        with open(filename, "r") as file:
            for line in file:
                task = line.strip()

                # Ignore blank lines and add non-empty tasks
                if task:
                    tasks.append(task)
    except FileNotFoundError:
        # A new project may not have a task file yet.
        return []

    return tasks


def save_tasks(tasks, filename):
    """Save all tasks to a text file."""
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")


def add_task(tasks):
    """Prompt the user for a task and add it to the task list."""
    task = input("Enter a new task: ").strip()

    if not task:
        print("A task cannot be empty.")
        return

    # Keep your existing append and confirmation code below
    tasks.append(task)
    print(f"Task added: {task}")


def view_tasks(tasks):
    """Display all tasks currently stored in the task list."""
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def remove_task(tasks):
    """Prompt the user to select and remove a task.

    Return True when a task is removed and False otherwise.
    """
    if not tasks:
        print("No tasks are available to remove.")
        return False

    view_tasks(tasks)
    selection = input("Enter the number of the task to remove: ").strip()

    if not selection.isdigit():
        print("Please enter a valid task number.")
        return False

    task_number = int(selection)

    if task_number < 1 or task_number > len(tasks):
        print("That task number does not exist.")
        return False

    # Subtract 1 because displayed numbers start at 1, but Python lists start at 0
    removed_task = tasks.pop(task_number - 1)

    print(f"Task removed: {removed_task}")

    return True


def main():
    """Run the TaskTrack menu until the user chooses to exit."""

    tasks = load_tasks(TASKS_FILE)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks, TASKS_FILE)
        elif choice == "3":
            if remove_task(tasks):
                save_tasks(tasks, TASKS_FILE)
        elif choice == "4":
            print("Exiting TaskTrack. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
     main()# peer review formatting update
