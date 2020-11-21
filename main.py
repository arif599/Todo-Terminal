# exceptions
class NotTitle(Exception):
    pass


class NotDescription(Exception):
    pass


class NotDueDate(Exception):
    pass


class NotPriority(Exception):
    pass


def catch_exceptions(function):
    def wrapper(*args):
        try:
            function(*args)
        except NotTitle:
            print("Title should be str.")
        except NotDescription:
            print("Description should be str.")
        except NotDueDate:
            print("Due Date should be Date.")
        except NotPriority:
            print("Priority should be str.")
    return wrapper

# Blueprint for Task objects


class Task:
    # constructor
    def __init__(self, title, description, dueDate, priority):
        # private variables
        self.set_title(title)
        self.set_description(description)
        self.set_dueDate(dueDate)
        self.set_priority(priority)

    # getters
    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_dueDate(self):
        return self._dueDate

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

    def set_priority(self, priority):
        self._priority = priority

    # methods
    def __str__(self):
        strTask = f"Task: {self.get_title()}"
        strDescription = f"Description: {self.get_description()}"
        strDueDate = f"Due Date: {self.get_dueDate()}"
        strPriority = f"Priority Level: {self.get_priority()}"

        return strTask + "\n" + strDescription + "\n" + strDueDate + "\n" + strPriority


def main():
    myTask = Task("HW", "NA", "11/20/2020", "High")
    print(myTask)


if __name__ == "__main__":
    main()
