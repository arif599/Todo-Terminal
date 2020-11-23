from task import Task
# Blueprint for User objects
class User:
    # constructor
    def __init__(self, id, firstName, lastName, email, password, title='', description='', dueDate='', createdDate='', priority='', taskId=0, completed=0):
        # private variables
        self.set_id(id)
        self.set_first_name(firstName)
        self.set_last_name(lastName)
        self.set_email(email)
        self.set_password(password)
        self.set_obj_task(title, description, dueDate, createdDate, priority, taskId, completed)


    # setters
    def set_id(self, id):
        self._id = id

    def set_first_name(self, firstName):
        self._firstName = firstName.strip().capitalize()
    
    def set_last_name(self, lastName):
        self._lastName = lastName.strip().capitalize()

    def set_email(self, email):
        self._email = email.strip().lower()
    
    def set_password(self, password):
        self._password = password

    def set_obj_task(self, title, description, dueDate, createdDate, priority, taskId=0, completed=0):
        self._obj_task = Task(title, description, dueDate, createdDate, priority, taskId, completed)

    # getters
    def get_id(self):
        return self._id

    def get_first_name(self):
        return self._firstName

    def get_last_name(self):
        return self._lastName

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_obj_task(self):
        return self._obj_task

    #methods
    def __str__(self):
        strId = f"User ID: {self.get_id()}"
        strFirstName = f"First Name: {self.get_first_name()}"
        strLastName = f"Last Name: {self.get_last_name()}"
        strEmail = f"Email: {self.get_email()}"
        strPassword = f"Password: {self.get_password()}"
        strTask = f"{self.get_obj_task()}"

        return strId+"\n"+strFirstName +"\n"+ strLastName +"\n"+ strEmail +"\n" + strPassword +"\n" + strTask

    # def save(self, db, mycursor):
    #     insertQuery = "INSERT INTO users(first_name, last_name, email, password) VALUES (%s, %s, %s, %s)" 
    #     mycursor.execute(insertQuery, (self.get_first_name(), self.get_last_name(), self.get_email(), self.get_password()))
    #     db.commit()
    
    # def authenticate(self, mycursor, userEmail, userPassword):
    #     findQuery = "SELECT id FROM users WHERE email=%s, password=%s"
    #     mycursor.execute(findQuery, (userEmail, userPassword))

    #     for x in mycursor:
    #         if x == "NULL":
    #             print(x)
    #             return False
    #         else:
    #             # store ID in a variable
    #             print(x)
    #             return True



    
