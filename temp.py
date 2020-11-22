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