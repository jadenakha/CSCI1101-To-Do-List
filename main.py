# Source - https://stackoverflow.com/a/2084628
# Posted by poke, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-23, License - CC BY-SA 3.0
# test

import os
def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')

# https://stackoverflow.com/questions/8953844/import-module-from-subfolder

from submodule import colors
# colors.BLUE
from submodule import addtask
# addtask.addtoday()
from submodule import checktask
# checktask.taskchecking()
# https://www.w3schools.com/python/python_datetime.asp

import datetime


# ===

schedule: dict[str, list[dict[str, str | bool]]] = {
    "Sunday": [
        {"task": "example", "checked": True},
        {"task": "example", "checked": False}                                     
    ],
    "Monday": [
        {"task": "example", "checked": True},
        {"task": "example", "checked": False}                                     
    ],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
}

schedule_days = list(schedule.keys())
today: str = datetime.datetime.now().strftime("%A") # returns today as string like "Wednesday"

togglePrints: dict[str, str] = {"view": "Today"}

def printChecks(keyValue: str) -> str:

    """
    Function for enumerating each day's tasks and current status on the check mark.
    "j" goes unused so that we can pull just the index value of schedule rather than
    the pure value of the index. 

    Parameters
    ----------
    keyValue : str
        Describes the value from the initial for loop. For example, in all for loops
        that this is nested under, "for k, v in enumerate(schedule_days):"
        where the v: str variable is the initial key Day, like "Sunday".

    Returns
    -------
    str
        Returns the status of each day's task as:
        print(f"{key + 1}. {checked} {schedule[keyValue][key]['task']}")
    """
    for key, value in enumerate(schedule[keyValue]): # for example schedule["Monday"]. i is the index for each in v (value)
        if schedule[keyValue][key]['checked'] == True:
            checked = f"{colors.green}[x]{colors.reset}"
        else:
            checked = f"{colors.red}[ ]{colors.reset}"
        print(f"{key + 1}. {checked} {schedule[keyValue][key]['task']}")  # 1. [ ] task

        due_date = schedule[keyValue][key].get("due_date")

        if due_date and due_date != "none":
            print(f"{colors.bold}Due: {due_date}{colors.reset}")
    
# print current day
def printToday() -> str:
    """
    First enumerates through schedule_days which is simplified to just return keys, or the weekdays.
    Works because they are in order of schedule, enumerating lets us specify if i want the index or value
    of the list.

    Returns only today.
    """
    print(f"== Today is: {today} ==")
    print()

    try:
        printChecks(today)
    except IndexError:
        print() # because otherwise theres no index in an empty table

# print all days, list

def printAllDays() -> str:
    """
    First enumerates through schedule_days which is simplified to just return keys, or the weekdays.
    Works because they are in order of schedule, enumerating lets us specify if i want the index or value
    of the list.

    Then, this basically becomes a loop over ALL days to do it in chronological order.
    """
    clearconsole()
    print()
    for k, v in enumerate(schedule_days):
        if schedule_days[k] == today:
            print(f"== Today: {schedule_days[k]} ==")
        else:
            print(f"== {schedule_days[k]} ==")
        print()

        try: 
            printChecks(v)
        except IndexError: # if theres an error and if its an index error then skips over otherwise full error
            print()

    print("== All Days and Tasks Above ==")
    print()


def settingsmenu() -> str:
    """
    Normal settings menu. Before I used to set a temporary value X, but realized
    I could have just returned it in the function. 

    Returns
    -------
    x
        X initializes input that is then stripped and lowercase so it can be consumed
        as something thats lowercase
    """
    print()
    print("What would you like to try and do?")
    print()
    print(f"'{colors.soft_purple}Add{colors.reset}' - {colors.chiffon_yellow}Adds a new task to a specified day.{colors.reset}")
    print(f"'{colors.pale_green}Check{colors.reset}' - {colors.chiffon_yellow}Modifies a check on a task from [X] to [ ], etc.{colors.reset}")
    print(f"'{colors.pastel_blue}List{colors.reset}' - {colors.chiffon_yellow}Toggles between printing today (default) or the entire list.{colors.reset}")
    print()

    x = str(input().strip().lower())
    return x


while True:
    clearconsole()
    if togglePrints["view"] == "Today":
        printToday()
    else:
        printAllDays()

    choice = settingsmenu()

    if choice == "add":
        addtask.addTask(schedule)
    elif choice == "check":
        checktask.taskchecking(schedule)
    elif choice == "list": # toggles the print from default of today to tmrw vise versa
        if togglePrints['view'] == "Today":
            togglePrints['view'] = "Tmrw"
        elif togglePrints['view'] == "Tmrw":
            togglePrints['view'] = "Today"
    else:
        print()
        print("Not available!")
        print()
