from task import Task
import datetime
from datetime import date

def main():
    #userLogin()
    task = createTask()

def userLogin():
    print("-------------LOGIN/REGISTER-------------")
    # user options
    print("1. Login")
    print("2. Register")
    userOption = int(input("Enter: "))

    if userOption == 1:
        pass

def createTask():
    print("------------CREATE YOUR TASK------------")
    wrongInput = False
    taskTitle = input("Enter Title: ")
    taskDescription = input("Enter Description: ")
    taskCreatedDate = date.today().strftime("%m/%d/%Y")
    while True:
        try:
            taskDueDate = input("Enter Due Date in MM/DD/YYYY: ")
            month, day, year = map(int, taskDueDate.split('/'))
            taskDueDate = datetime.date(year, month, day).strftime("%m/%d/%Y")
            break
        except ValueError:
            print("Your input for Data is incorrect. Please enter a valid Date.\n")
            wrongInput = True
            continue

    while True:  
        taskPriority = input("Enter Priority (High, Medium, or Low): ").lower().strip()
        if taskPriority not in ["high", "medium", "low"]:
            print("Your input for Priority is incorrect. Please enter a valid response.\n")
            wrongInput = True
            continue
        break

    userTask = Task(taskTitle, taskDescription, taskCreatedDate, taskDueDate, taskPriority)
    if wrongInput:
        print(f"\nYour final task input:\n{userTask}")
    print("Task has been succefully created.")
    print("-----------------------------------------")
    return userTask

if __name__ == "__main__":
    main()
