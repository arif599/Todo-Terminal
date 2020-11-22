# Blueprint for User objects
class User:
    # constructor
    def __init__(self, firstName, lastName, email, password):
        # private variables
        self.set_first_name(firstName)
        self.set_last_name(lastName)
        self.set_email(email)
        self.set_password(password)

    # getters
    def get_first_name(self):
        return self._firstName

    def get_last_name(self):
        return self._lastName

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    # setters
    def set_first_name(self, firstName):
        self._firstName = firstName.strip().capitalize()
    
    def set_last_name(self, lastName):
        self._lastName = lastName.strip().capitalize()

    def set_email(self, email):
        self._email = email.strip().lower()
    
    def set_password(self, password):
        self._password = password

    #methods
    def __str__(self):
        strFirstName = f"First Name: {self.get_first_name()}"
        strLastName = f"Last Name: {self.get_last_name()}"
        strEmail = f"Email: {self.get_email()}"
        strPassword = f"Password: {self.get_password()}"

        return strFirstName +"\n"+ strLastName +"\n"+ strEmail +"\n" + strPassword

    def save(self, db, mycursor):
        insertQuery = "INSERT INTO users(first_name, last_name, email, password) VALUES (%s, %s, %s, %s)" 
        mycursor.execute(insertQuery, (self.get_first_name(), self.get_last_name(), self.get_email(), self.get_password()))
        db.commit()

    
