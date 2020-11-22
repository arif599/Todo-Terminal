from task import Task
import datetime
from datetime import date
import mysql.connector
import config
from user import User

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
    authenticate_user()
    #tasks_main()


def authenticate_user():
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

        if userOption == 1:
            login()
            break
        elif userOption == 2:
            createUser()
            login()
            break
        else:
            print("You entered a number that is not in the given options. Try selecting either 1 or 2.")
            continue

def login():
    pass

def createUser():
    print("----------------REGISTER----------------")
    userFirstName = input("Enter your first name: ")
    userLastName = input("Enter your last name: ")
    # check to see it user entered a valid email
    userEmail = input("Enter your email: ")
    # check if strong password and maybe encrypt it
    userPassword = input("Enter a password: ")

    newUser = User(userFirstName, userLastName, userEmail, userPassword)
    newUser.save(db, mycursor)
    print("You have been succefully registered!")



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

    userTask = Task(taskTitle, taskDescription, taskDueDate, taskCreatedDate, taskPriority)
    if wrongInput:
        print(f"\nYour final task input:\n{userTask}")
    print("Task has been succefully created.")
    print("-----------------------------------------")
    return userTask

if __name__ == "__main__":
    main()
