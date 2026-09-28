from submodule import addtask
# addtask.addtoday()
from submodule import checktask
# checktask.taskchecking()


def settingsmenu(printDays, schedule, schedule_days, printToday, togglePrints): # because printdays is a function in main you have to pass it through

    if togglePrints['view'] == "Today":
        printToday()
    else:
        printDays()

    print()
    print("What would you like to try and do?")
    print()
    print("'Add' - Adds a new task to the current day.")
    print("'Check' - Modifies a check on a task from [X] to [ ], etc.")
    print("'List' Toggles between printing today (default) or the entire list.")
    print()

    x = str(input().strip().lower())                                                            # Input a string for everything below:

    if x == "add":
        addtask.addtoday(printDays, schedule, schedule_days, printToday, togglePrints)
    elif x == "check":
        checktask.taskchecking(printDays, schedule, schedule_days, printToday, togglePrints)
    elif x == "list": # toggles the print from default of today to tmrw vise versa
        if togglePrints['view'] == "Today":
            togglePrints['view'] = "Tmrw"
        elif togglePrints['view'] == "Tmrw":
            togglePrints['view'] = "Today"
    else:
        print()
        print("Not available!")
        print()
