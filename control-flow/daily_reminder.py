task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

match priority:
    case "high":
        reminder = f"Your HIGH priority task is: {task}."
    case "medium":
        reminder = f"Your MEDIUM priority task is: {task}."
    case "low":
        reminder = f"Your LOW priority task is: {task}."
    case _:
        reminder = f"Task: {task}. (Unknown priority level entered.)"

if time_bound == "yes":
    reminder += " This task requires immediate attention today!"
print(reminder)
