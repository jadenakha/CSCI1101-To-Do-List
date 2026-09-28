# Source - https://stackoverflow.com/a/2084628
# Posted by poke, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-23, License - CC BY-SA 3.0

import os
def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')

# https://stackoverflow.com/questions/8953844/import-module-from-subfolder

from submodule import addtask
# addtask.addtoday()
from submodule import defaultsettings
# defaultsettings.settingsmenu()
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
today = datetime.datetime.now().strftime("%A")
total_tasks = list(schedule.values())
# print(schedule["Monday"][0]) # {'task': 'example', 'checked': True}
# print(schedule["Monday"][0]["task"]) # return "example"
# print(schedule["Monday"][0]["checked"]) # return True

while True:
    # print current day
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
    def printAllDays():
        clearconsole()
        print()
        for k, v in enumerate(schedule_days):
            if schedule_days[k] == today:
                print(f"== Today: {schedule_days[k]} ==")
            else:
                print(f"== {schedule_days[k]} ==")
            print()
            try: # learned try blocks from boot.dev however https://www.w3schools.com/python/python_try_except.asp
                for i, j in enumerate(schedule[v]):
                    if schedule[v][i]['checked'] == True:
                        x = "[x]"
                    else:
                        x = "[ ]"

                    print(f"{i + 1}. {x} {schedule[v][i]['task']}")
                print()
            except IndexError:
                print()
        print("== All Days and Tasks Above ==")
        print()

    defaultsettings.settingsmenu(printAllDays, schedule)

