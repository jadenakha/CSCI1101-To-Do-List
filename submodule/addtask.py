def addTask(schedule):
    """
    Essentially, if you want to add a task to a day you
    - Declare what day you want to add to first
    - Check if it's okay
    - If it's fine, 

    Parameters
    ----------
    schedule: dict[str, list[str | bool]]
        Original schedule in main imported basically. Since that's all we kinda used anyways in the func

    Returns
    -------
    Basically returns nothing, because then the loop in main essentailly continues on 
    """
    import datetime
    addnew = str(input("To what day would you like to add (caps sensitive, like 'Monday')? Type 'exit' to return back to options: "))

    if addnew not in schedule: # Checks if its a valid typed day
        print("Not a valid day!") # id rather not raise an error and break the loop, just move them back
        return
    elif addnew == "exit":
        return

    taskName = str(input(f"What task would you like to add for {addnew}?: "))
    while True:
        due_date = input("Enter a due date (MM/DD/YYYY) or type 'none': ")
        if due_date == "none":
            break
        try:
            datetime.datetime.strptime(due_date, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format! Please use YYYY-DD-MM.")
    try:
        schedule[addnew].append({"task": taskName, "checked": False}) # Appends
        schedule[addnew][-1]["due_date"] = due_date
    except: # If there's any error notify in case something is bad with something but doesnt break app here 
        print("Error?")
        print()
        return

    
