def taskchecking(schedule: dict[str, list[str | bool]]):
    """
    Holds the function for checking tasks existing and if you would like to edit tasks. Does a few things:
    - Checkstatus asks for a specific day, following function checks if the day exists
    - Statuscheck then does the operation of checking or unchecking a specific task
    - Then contained loop at the bottom which is essentially the operation of modifycheck etc after
    all the base conditions above basically pass

    Reason why I didn't declare def taskchecking() -> str is because return technically doesn't return anything,
    so pylance got mad which makes sense


    Parameters
    ----------
    schedule: dict[str, list[str | bool]]
        Original schedule in main imported basically. Since that's all we kinda used anyways in the func

    Returns
    -------
    Basically returns nothing, because then the loop in main essentailly continues on 
    """
    checkstatus = str(input("What day would you like to edit the tasks in (caps sensitive, like 'Monday')? Type 'exit' to return back to options: "))

    if checkstatus not in schedule: # checks if in schedule (day like Monday rejects monday cuz not proper typed) otherwise returns
        print("Day not in schedule! Check caps!")
        return
    elif checkstatus == "exit":
        return

    def statuscheck(): # [checkstatus - 1] because we don't want the possibility of "0" even though index starts at 0 we display as 1 starting
        if schedule[checkstatus][modifyCheck - 1]["checked"] == True:
            schedule[checkstatus][modifyCheck - 1]["checked"] = False
            print("Unchecked!")
        else:
            schedule[checkstatus][modifyCheck - 1]["checked"] = True
            print("Checked!")

    try:
        modifyCheck = int(input("What task would you like to check or uncheck from that day? "))
        if modifyCheck > 0 and modifyCheck <= len(schedule[checkstatus]): # if it's not 0 (expect 1 and above) and less than or = to length (1 minimum, also bounds)
            statuscheck()
    except (IndexError, ValueError): # handles invalid task numbers
        print("Not a valid task #")
        print()
        return
