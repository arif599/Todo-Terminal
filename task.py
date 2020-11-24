# Blueprint for Task objects
class Task:
    # constructor
    def __init__(self, title, description, due_date, created_date, priority, taskId=0, completed=0):
        # private variables
        self.set_task_id(taskId)
        self.set_title(title)
        self.set_description(description)
        self.set_due_date(due_date)
        self.set_created_date(created_date)
        self.set_priority(priority)
        self.set_completed(completed)

    # setters
    def set_task_id(self, taskId):
        self._taskId = taskId

    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description

    def set_due_date(self, due_date):
        self._due_date = due_date

    def set_created_date(self, created_date):
        self._created_date = created_date

    def set_priority(self, priority):
        self._priority = priority

    def set_completed(self, completed):
        self._completed = completed

    # getters
    def get_task_id(self):
        return self._taskId

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_due_date(self):
        return self._due_date

    def get_created_date(self):
        return self._created_date

    def get_priority(self):
        return self._priority
    
    def get_completed(self):
        return self._completed





    # methods
    def __str__(self):
        #strTaskId = f"Task ID: {self.get_task_id()}"
        strTask = f"Task: {self.get_title()}"
        strDescription = f"Description: {self.get_description()}"
        strcreated_date = f"Created Date: {self.get_created_date()}"
        strdue_date = f"Due Date: {self.get_due_date()}"
        strPriority = f"Priority Level: {self.get_priority()}"
        if self.get_completed() == 1:
            strCompleted = f"This task is COMPLETED"
        else:
            strCompleted = f"This task is NOT COMPLETED"

        #return strTaskId +"\n"+ strTask + "\n" + strDescription + "\n" + strcreated_date + "\n" + strdue_date + "\n" + strPriority +"\n"+ strCompleted
        return strTask + "\n" + strDescription + "\n" + strcreated_date + "\n" + strdue_date + "\n" + strPriority +"\n"+ strCompleted
