# Blueprint for Task objects
class Task:
    # constructor
    def __init__(self, title, description, dueDate, createdDate, priority):
        # private variables
        self.set_title(title)
        self.set_description(description)
        self.set_dueDate(dueDate)
        self.set_createdDate(createdDate)
        self.set_priority(priority)

    # getters
    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_dueDate(self):
        return self._dueDate

    def get_createdDate(self):
        return self._createdDate

    def get_priority(self):
        return self._priority


    # setters
    def set_title(self, title):
        # if not isinstance(title, str):
        #     print("Throwing NotTitle")
        #     raise NotTitle
        self._title = title

    def set_description(self, description):
        self._description = description

    def set_dueDate(self, dueDate):
        self._dueDate = dueDate

    def set_createdDate(self, createdDate):
        self._createdDate = createdDate

    def set_priority(self, priority):
        self._priority = priority



    # methods
    def __str__(self):
        strTask = f"Task: {self.get_title()}"
        strDescription = f"Description: {self.get_description()}"
        strCreatedDate = f"Created Date: {self.get_createdDate()}"
        strDueDate = f"Due Date: {self.get_dueDate()}"
        strPriority = f"Priority Level: {self.get_priority()}"

        return strTask + "\n" + strDescription + "\n" + strCreatedDate + "\n" + strDueDate + "\n" + strPriority
