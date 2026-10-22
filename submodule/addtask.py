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

    addnew = str(input("To what day would you like to add (caps sensitive, like 'Monday')? Type 'exit' to return back to options: "))

    if addnew not in schedule: # Checks if its a valid typed day
        print("Not a valid day!") # id rather not raise an error and break the loop, just move them back
        return
    elif addnew == "exit":
        return

    taskName = str(input(f"What task would you like to add for {addnew}?: "))
    try:
        schedule[addnew].append({"task": taskName, "checked": False}) # Appends
    except: # If there's any error notify in case something is bad with something but doesnt break app here 
        print("Error?")
        print()
        return
