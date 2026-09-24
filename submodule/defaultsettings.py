from submodule import addtask
# addtask.addtoday()
from submodule import checktask
# checktask.taskchecking()

def settingsmenu():                                                          # The Default Interaction (moves through all things below)
    print()
    print("What would you like to try and do?")
    print()
    print("'Add' - Adds a new task to the current day.")
    print("'Check' - Modifies a check on a task from [X] to [ ], etc.")
    print()

    x = str(input().strip().lower())                                                            # Input a string for everything below:

    if x == "add":
        addtask.addtoday()
    elif x == "check":
        checktask.taskchecking()
    else:
        print()
        print("Not available!")
        print()
