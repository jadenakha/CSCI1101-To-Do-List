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

schedule: dict[str, list[str | bool]] = {
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
        for key, value in enumerate(schedule[today]):
            if schedule[today][key]['checked'] == True:
                checked = "[x]"
            else:
                checked = "[ ]"
            print(f"{key + 1}. {checked} {schedule[today][key]['task']}")
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
            for i, j in enumerate(schedule[v]): # for example schedule["Monday"]. i is the index for each in v (value)
                if schedule[v][i]['checked'] == True:
                    x = "[x]"
                else:
                    x = "[ ]"

                print(f"{i + 1}. {x} {schedule[v][i]['task']}")  # 1. [ ] task
            print()
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
    print("Add - Adds a new task to a specified day.")
    print("'Check' - Modifies a check on a task from [X] to [ ], etc.")
    print("'List' Toggles between printing today (default) or the entire list.")
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
