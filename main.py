import datetime
from datetime import date
import mysql.connector
import config
from user import User
from task import Task

db = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    database=config.database
)
mycursor = db.cursor()
# mycursor.execute('INSERT INTO users(Name, UnlockCount) VALUES ("hello", 5);')
# db.commit()

def main():
    #userLogin()
    #createTask(userID)
    #task = createTask()
    clientId = prompt_user()
    client = load_user(clientId)
    # print("-------LOADED USER---------")
    # print(client)
    # print("---------------------------")
    prompt_user_options(client)
    #print(client)
    #prompt_user_option(client)
    
    #tasks_main()
def prompt_user_options(user):
    print(f"----------------WELCOME {user.get_first_name().upper()}----------------")
    viewTasks = False
    taskMap = {}

    while True:
        if not viewTasks:
            print("Select an option")
            print("0. Logout/quit")
            print("1. Create a new task")
            print("2. View all tasks")
            print("3. View current tasks")
            print("4. View completed tasks")
            userInput = int(input("Enter: "))
        else:
            print("Select an option")
            print("1. Create a new task")
            print("2. View all tasks")
            print("3. View current tasks")
            print("4. View completed tasks")
            print("5. Edit a task")
            print("6. Delete a task")
            print("7. Mark a task complete")
            userInput = int(input("Enter: "))


        if userInput == 1:
            #clientTask = createTask(user)
            print("------------CREATE YOUR TASK------------")
            createTask(user)
            #print(user)
        elif userInput == 2:
            taskMap = prompt_tasks_view(user, "all")
            viewTasks = True
        elif userInput == 5 and viewTasks == True:
            editTask = int(input("Select a task to edit: "))
            loadedTask = load_task(taskMap[editTask])
            print("1) edit all")
            print("2) edit title")
            print("3) edit description")
            print("4) edit created date")
            print("5) edit due date")
            print("6) edit priority")
            print("7) edit completed status:")
            editOption = int(input("Enter: "))
            task_update(user, editOption, loadedTask)
            print("------------EDIR YOUR TASK------------")

def load_task(taskId):
    loadQuery = f"SELECT * FROM tasks WHERE task_id={taskId}"
    mycursor.execute(loadQuery)
    taskRow = mycursor.fetchone()
    return Task(taskRow[2], taskRow[3], taskRow[5], taskRow[4], taskRow[6], taskRow[0], taskRow[7]) 
    
def task_update(user, userOption, loadedTask):
    taskId = loadedTask.get_task_id()
    if userOption == 1:
        createTask(user, taskId)
        updateTaskQuery = f"UPDATE tasks SET title=%s, description=%s, created_date=%s, due_date=%s, priority=%s, completed=%s WHERE task_id = {taskId}"
        mycursor.execute(updateTaskQuery, (user.get_obj_task().get_title(), user.get_obj_task().get_description(), user.get_obj_task().get_created_date(), user.get_obj_task().get_due_date(), user.get_obj_task().get_priority(), user.get_obj_task().get_completed()))
        db.commit()
        print("Task have been updated")


def prompt_tasks_view(user, viewStatus):
    taskMap = {}

    if viewStatus == "all":
        viewAllQuery = "SELECT * FROM tasks WHERE user_id=%s"
        mycursor.execute(viewAllQuery, (user.get_id(),))
        for i, task in enumerate(mycursor, 1):
            user.set_obj_task(task[2], task[3], task[5], task[4], task[6], task[7])
            taskMap[i] = task[0]
            print(f"{i}){user.get_obj_task()}\n")

    #prompt_tasks_edit(user, taskMap)
    print(taskMap)
    return taskMap

# def prompt_tasks_edit(user, taskMap):
#     print("1) Edit a task")
#     print("2) Return home")
#     userInput = input("1) Edit a task")

#     if userInput == 1:
#         print()



def prompt_user():
    print("-------------LOGIN/REGISTER-------------")

    while True:
        try:
            # user options
            print("1. Login")
            print("2. Register")
            userOption = int(input("Enter: "))
        except ValueError:
            print("Your input for Options is wrong. Please enter a valid number.")
            continue
        
        # try putting just return instaed of userID return login()
        if userOption == 1:
            userID = login()
            break
        elif userOption == 2:
            createUser()
            userID = login()
            break
        else:
            print("You entered a number that is not in the given options. Try selecting either 1 or 2.")
            continue
    return userID

def login():
    print("----------------LOGIN----------------")
    while True:
        userEmail = input("Enter your email: ").strip()
        userPassword = input("Enter your password: ")

        #if user exits then populate user object
        findQuery = "SELECT IFNULL((SELECT id FROM users WHERE email=%s AND password=%s) , false)"
        mycursor.execute(findQuery, (userEmail, userPassword))
        
        
        for x in mycursor:
            userID = x
            break

        if userID[0]==0:
            print("Your username or password is wrong. Try again.\n")
            continue
            #return False
            #continue
        else:
            # store ID in a variable
            return userID[0]
            # print(userID[0])
            # break
            #send userId to populate user obj
            #return True
        
    #return obj or pass to function that creates one


def load_user(userId):
    loadQuery = f"SELECT * FROM users WHERE id={userId}"
    mycursor.execute(loadQuery)
    row = mycursor.fetchone()
    return User(row[0], row[1], row[2], row[3], row[4]) 


def createUser():
    print("----------------REGISTER----------------")
    userFirstName = input("Enter your first name: ").strip().capitalize()
    userLastName = input("Enter your last name: ").strip().capitalize()
    # check to see it user entered a valid email
    userEmail = input("Enter a email: ").strip()
    # check if strong password and maybe encrypt it
    userPassword = input("Enter a password: ")

    insertUserQuery = "INSERT INTO users(first_name, last_name, email, password) VALUES (%s, %s, %s, %s)" 
    mycursor.execute(insertUserQuery, (userFirstName, userLastName, userEmail, userPassword))
    db.commit()

    #newUser = User(userFirstName, userLastName, userEmail, userPassword)
    print("You have been succefully registered!\n")
    #return newUSer



def createTask(user, editTaskId=None):
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

    #userTask = Task(taskTitle, taskDescription, taskDueDate, taskCreatedDate, taskPriority)
    user.set_obj_task(taskTitle, taskDescription, taskDueDate, taskCreatedDate, taskPriority)

    if editTaskId is not None:
        while True:  
            taskCompletionStatus = input("Enter completion status (Done, Not Done): ").lower().strip()
            if taskCompletionStatus == "done":
                taskCompletionStatus = 1
            elif taskCompletionStatus == "not done":
                taskCompletionStatus = 0
            else:
                print("Your input for Completed status is incorrect. Please enter a valid response.\n")
                continue
            break
        user.set_obj_task(taskTitle, taskDescription, taskDueDate, taskCreatedDate, taskPriority, editTaskId, taskCompletionStatus)
        return

    if wrongInput:
        print(f"\nYour final task input:\n{user.task()}")
    print("Task has been succefully created.")

    insertTaskQuery = "INSERT INTO tasks(user_id, title, description, created_date, due_date, priority) VALUES(%s, %s, %s, %s, %s, %s)"
    mycursor.execute(insertTaskQuery, (user.get_id(), taskTitle, taskDescription, taskDueDate, taskCreatedDate, taskPriority))
    db.commit()
    user.get_obj_task().set_task_id(mycursor.lastrowid)
    #print(user.get_obj_task())
    print("-----------------------------------------")

if __name__ == "__main__":
    main()
