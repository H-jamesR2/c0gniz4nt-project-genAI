import datetime
import json

DATA_FILE = "study_planner_data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"tasks": [], "scores": {}}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, default=str, indent=4)

def get_valid_date(prompt):
    while True:
        try:
            date_str = input(prompt)
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_valid_int(prompt, min_val=1, max_val=10):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add_task(tasks):
    task_name = input("Enter task name: ")
    deadline = get_valid_date("Enter deadline (YYYY-MM-DD): ")
    priority = get_valid_int("Enter priority (1-10, 1 = highest): ", 1, 10)
    tasks.append({"name": task_name, "deadline": deadline, "priority": priority})
    print("Task added successfully!\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    sorted_tasks = sorted(tasks, key=lambda x: (x['priority'], x['deadline']))
    print("\nTask List (Sorted by Priority & Deadline):")
    for task in sorted_tasks:
        print(f"{task['name']} - Due: {task['deadline']} - Priority: {task['priority']}")
    print()

def add_score(scores):
    subject = input("Enter subject name: ")
    score = get_valid_int("Enter your score (0-100): ", 0, 100)
    if subject not in scores:
        scores[subject] = []
    scores[subject].append(score)
    print("Score added successfully!\n")

def view_scores(scores):
    if not scores:
        print("No scores recorded.")
        return
    print("\nPerformance Overview:")
    for subject, marks in scores.items():
        avg_score = sum(marks) / len(marks)
        score_status = ""
        if avg_score < 50:
            score_status = 'Weak'
        elif avg_score < 75:
            score_status = 'Needs To Do Better!'
        else:
            score_status = 'Good'
        print(f"{subject}: Avg Score = {avg_score:.2f} ({score_status})")
    print()

def main():
    data = load_data()
    tasks = data["tasks"]
    scores = data["scores"]
    
    while True:
        print("\nStudy Planner Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Add Score")
        print("4. View Scores")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            add_score(scores)
        elif choice == "4":
            view_scores(scores)
        elif choice == "5":
            save_data({"tasks": tasks, "scores": scores})
            print("Data saved. Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
