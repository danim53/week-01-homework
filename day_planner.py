"""This program is a day planner
first it asks a user for a name and three tasks
then prints a numbered list of tasks to the screen"""
def main() -> None:
    #get user input
    name = input("Please enter your name: ".strip())
    #create empty task list
    task = []

    #ask for 3 tasks in loop
    for i in range(1, 4):
        task.append(input(f"Please enter your task {i}: ".strip()))

    print(f"Here are your tasks for today, {name}")

    #print numbered list
    for number, task in enumerate(task, 1):
        print(f"{number}. {task}".strip())

if __name__ == "__main__":
    main()