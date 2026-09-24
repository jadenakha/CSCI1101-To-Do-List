# https://stackoverflow.com/questions/8953844/import-module-from-subfolder

from submodule import addtask
# addtask.addtoday()
from submodule import defaultsettings
# defaultsettings.settingsmenu()
from submodule import checktask
# checktask.taskchecking()

# Source - https://stackoverflow.com/a/2084628
# Posted by poke, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-23, License - CC BY-SA 3.0

import os
def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')

# ===

day: str = "Monday"

schedule: dict[str, list[dict[str, bool]]] = {                                  # str | bool makes pylance happy
    "Monday": [
        {"task": "example", "checked": True}                                    # list[dict[str, bool]] so monday[0] -> 
    ]
}

schedule_days = list(schedule.keys())
total_tasks = list(schedule.values())
# print(schedule["Monday"][0]) # {'task': 'example', 'checked': True}
# print(schedule["Monday"][0]["task"]) # return "example"
# print(schedule["Monday"][0]["checked"]) # return True

while True:
    clearconsole()
    print(f"== {schedule_days[0]} ==")
    displayed_day: str = schedule_days[0]                                       # sets as "monday" from list of scheduled_days for now
    def check():
        if schedule[displayed_day][i]["checked"] == True:                       # [x] or [ ] for iterate below
            return "x"
        else:
            return " "

    i: int = 0
    while i < len(schedule[displayed_day]):                                     # length of schedule -> monday -> length of list 
        print(f"{i + 1}. [{check()}] {schedule[displayed_day][i]['task']}")     # i + 1 so we don't state "0"
        i += 1

    defaultsettings.settingsmenu()

