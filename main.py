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
    print("----------------WELCOME----------------")
    print("Select an option")
    print("1. Create a new task")
    print("2. View all tasks")
    print("3. View current tasks")
    print("4. View completed tasks")
        # print(" View all taks")
        # print("Select a task to edit")
    print("3. sign out")
    userInput = int(input("Enter: "))

    if userInput == 1:
        #clientTask = createTask(user)
        createTask(user)
        print(user)
    elif userInput == 2:
        prompt_tasks_view(user, "completed")
        pass



def prompt_tasks_view(user, viewStatus):
    pass

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



def createTask(user):
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

    #userTask = Task(taskTitle, taskDescription, taskDueDate, taskCreatedDate, taskPriority)
    user.set_obj_task(taskTitle, taskDescription, taskDueDate, taskCreatedDate, taskPriority)

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
