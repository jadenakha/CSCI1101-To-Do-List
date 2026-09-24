# data
# "add multiple values to one key" 
# research: dict only points single object,
# must set as container type
# namedtuples are immutable unfortunately
# set it as a list and nest a dict? so
# schedule[monday[0][bool]]
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

# ===

def defaultsettings():                                                          # The Default Interaction (moves through all things below)
    print()
    print("What would you like to try and do?")
    print()
    print("'Add' - Adds a new task to the current day.")
    print("'Check' - Modifies a check on a task from [X] to [ ], etc.")
    print()

    x = str(input()).strip().lower()                                                            # Input a string for everything below:

    if x == "add":
        addtoday()
    elif x == "check":
        taskchecking()
    else:
        print()
        print("Not available!")
        print()

def taskchecking():
    checkstatus = input("Would you like to check / uncheck something? Type 'exit' to return back to options: ")
    if checkstatus == "exit":
        # x = str(input("What would you like to try and do? Available: 'Add' or 'Check' to check something off?"))
        defaultsettings()

    def statuscheck(checkstatus):                                               # [checkstatus - 1] because we don't want the possibility of "0"
        if schedule[displayed_day][checkstatus - 1]["checked"] == True:
            schedule[displayed_day][checkstatus - 1]["checked"] = False
            print("Unchecked!")
        else:
            schedule[displayed_day][checkstatus - 1]["checked"] = True
            print("Checked!")

    if checkstatus > 0 and checkstatus <= len(schedule[displayed_day]):         # if it's not 0 (expect 1 and above) and less than or = to length (1 minimum, also bounds)
        statuscheck(checkstatus)
    else:
        print("Doesn't Exist")

def addtoday():
    addnew = str(input("What would you like to add? Type 'exit' to return back to options: "))

    if addnew == "exit":
        # x = str(input("What would you like to try and do? Available: 'Add' or 'Check' to check something off?"))
        defaultsettings()
    else:
        schedule[displayed_day].append({"task": addnew, "checked": False})

# ===

while True:
    print(f"== {schedule_days[0]} ==")
    displayed_day: str = schedule_days[0]                                       # sets as "monday" from list of scheduled_days for now
    def check():
        if schedule[displayed_day][i]["checked"] == True:                       # [x] or [ ] for iterate below
            return("x")
        else:
            return(" ")

    i: int = 0
    while i < len(schedule[displayed_day]):                                     # length of schedule -> monday -> length of list 
        print(f"{i + 1}. [{check()}] {schedule[displayed_day][i]['task']}")     # i + 1 so we don't state "0"
        i += 1

    defaultsettings()

