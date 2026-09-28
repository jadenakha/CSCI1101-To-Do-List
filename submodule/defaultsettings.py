from submodule import addtask
# addtask.addtoday()
from submodule import checktask
# checktask.taskchecking()

def settingsmenu(printDays, schedule): # because printdays is a function in main you have to pass it through
    print()
    print("What would you like to try and do?")
    print()
    print("'Add' - Adds a new task to the current day.")
    print("'Check' - Modifies a check on a task from [X] to [ ], etc.")
    print("'List' lists all days and tasks.")
    print()

    x = str(input().strip().lower())                                                            # Input a string for everything below:

    if x == "add":
        addtask.addtoday(schedule)
    elif x == "check":
        checktask.taskchecking(schedule)
    elif x == "list":
        printDays()
    else:
        print()
        print("Not available!")
        print()
