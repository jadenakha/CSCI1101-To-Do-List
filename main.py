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

today: str = datetime.datetime.now().strftime("%A") # returns today as string like "Wednesday"
togglePrints: dict[str, str] = {"view": "Today"}

def printChecks(selectedDay: str, dataDict: dict[str, list[dict[str, str | bool]]]) -> None:

    """
    Function for enumerating each day's tasks and current status on the check mark.
    "j" goes unused so that we can pull just the index value of schedule rather than
    the pure value of the index. 

    Serves as the "base condition" and iterative loop for each individual day so that
    things inside the day can be returned consistently throughout all loops.

    Parameters
    ----------
    selectedDay : str
        Describes the value from the initial for loop. For example, in all for loops
        that this is nested under, "for k, v in enumerate(schedule_days):"
        where the v: str variable is the initial key Day, like "Sunday".
    dataDict : dict[str, list[dict[str, str  |  bool]]]
        Expects that the original dictionary is formatted this way. Done to contain
        the scope within the function, or modularity.
    """

    for key, value in enumerate(dataDict[selectedDay]): # for example schedule["Monday"]. i is the index for each in v (value)
        if dataDict[selectedDay][key]['checked'] is True:
            checked = f"{colors.green}[x]{colors.reset}"
        else:
            checked = f"{colors.red}[ ]{colors.reset}"
    
        print(f"{key + 1}. {checked} {dataDict[selectedDay][key]['task']}")  # 1. [ ] task

        due_date = dataDict[selectedDay][key].get("due_date")

        if due_date and due_date != "none":
            print(f"{colors.bold}Due: {due_date}{colors.reset}")
    
# print current day
def printSelectedDay(typeOfDay: str, selectedDay: str, dataDict: dict[str, list[dict[str, str | bool]]]) -> None:

    """
    Isolates an individual day to expand it's tasks and statuses.

    Parameters
    ----------
    selectedDay : str
        Describes the value from the initial for loop. For example, in all for loops
        that this is nested under, "for k, v in enumerate(schedule_days):"
        where the v: str variable is the initial key Day, like "Sunday".
    dataDict : dict[str, list[dict[str, str  |  bool]]]
        Expects that the original dictionary is formatted this way. Done to contain
        the scope within the function, or modularity.
    typeOfDay : str
        So that the type of day becomes malleable. Can be "today" or can be "selected day"
        or any other declared thing.
    """

    print(f"== {typeOfDay} is: {selectedDay} ==")
    print()

    printChecks(selectedDay, dataDict)

# print all days, list

def printAllDays(dataDict: dict[str, list[dict[str, str | bool]]]) -> None:

    """
    Substantiates the for loop for iterating through ALL days sequentially.

    Parameters
    ----------
    dataDict : dict[str, list[dict[str, str  |  bool]]]
        _description_
    """

    clearconsole()
    print()

    schedule_days: list[str] = list(dataDict.keys()) # Used so we can enumerate and separate index (key) from value.

    for key, value in enumerate(schedule_days):
        if schedule_days[key] == today: # ONLY for today
            print(f"== Today: {schedule_days[key]} ==")
        else:
            print(f"== {schedule_days[key]} ==")
        print()
        printChecks(value, dataDict)
        print()

    print("== All Days and Tasks Above ==")
    print()

def settingsmenu() -> None:
    """
    Normal settings menu print. Able to be reused and easily modified
    for any settings / options available.
    """

    print(f"'{colors.soft_purple}Add{colors.reset}' - {colors.chiffon_yellow}Adds a new task to a specified day.{colors.reset}")
    print(f"'{colors.pale_green}Check{colors.reset}' - {colors.chiffon_yellow}Modifies a check on a task from [X] to [ ], etc.{colors.reset}")
    print(f"'{colors.pastel_blue}List{colors.reset}' - {colors.chiffon_yellow}Toggles between printing today (default) or the entire list.{colors.reset}")
    print()

if __name__ == "__main__":
    while True:
        clearconsole()
        if togglePrints["view"] == "Today":
            printSelectedDay("Today", today, schedule)
        else:
            printAllDays(schedule)

        print()
        print("What would you like to try and do?")
        print()

        settingsmenu()
        choice = str(input().strip().lower())

        if choice == "add":
            print(addtask.addTask(schedule))
        elif choice == "check":
            checktask.taskchecking(schedule)
        elif choice == "list": # toggles the print from default of today to tmrw vise versa
            if togglePrints['view'] == "Today":
                togglePrints['view'] = "Tmrw"
            elif togglePrints['view'] == "Tmrw":
                togglePrints['view'] = "Today"
        else:
            print()
            print("Not an available option! Please reference available items: ")
            print()
