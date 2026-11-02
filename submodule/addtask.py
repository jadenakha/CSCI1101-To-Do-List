import datetime

def addTask(schedule: dict[str, list[dict[str, str | bool]]]) -> None:

    """
    Essentially, if you want to add a task to a day you
    - Declare what day you want to add to first
    - Check if it's okay and in schedule
    - Ask for a potential due date / note

    Parameters
    ----------
    schedule: dict[str, list[dict[str, str | bool]]]
        Original schedule in main imported basically. Since that's all we kinda used anyways in the func
    """

    while True:
        addnew: str = str(input("To what day would you like to add (caps sensitive, like 'Monday')? Type 'exit' to return back to options: "))

        if addnew == "exit":
            return
        elif addnew in schedule: # Checks if its a valid typed day
            break
        else:
            print("Not a valid option!")


    taskName: str = input(f"What task would you like to add for {addnew}?: ")
 
    due_date: str = input("Enter a due date (MM/DD/YYYY) or type 'none': ")

    if due_date != "none":
        try:
            datetime.datetime.strptime(due_date, "%m/%d/%Y")
        except ValueError: # because we only expect mm/dd/yyyy, not 01-10-1010
            print("Invalid date! Please use MM/DD/YYYY.")
            return

    schedule[addnew].append({"task": taskName, "checked": False}) # Appends
    schedule[addnew][-1]["due_date"] = due_date
