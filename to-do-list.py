# data
# "add multiple values to one key" 
# research: dict only points single object,
# must set as container type
# namedtuples are immutable unfortunately
# set it as a list and nest a dict? so
# schedule[monday[0][bool]]
day: str = "Monday"

schedule: dict[str, list[dict[str, bool]]] = {
    "Monday": [
        {"task": "example", "checked": True} # list[dict[str, bool]] so monday[0] -> 
    ]
}

schedule_days = list(schedule.keys())

# print(schedule["Monday"][0]) # {'task': 'example', 'checked': True}
# print(schedule["Monday"][0]["task"]) # return "example"
# print(schedule["Monday"][0]["checked"]) # return True


while True:
    print(f"== {schedule_days[0]} ==")
    displayed_day: str = schedule_days[0]

    def check():
        if schedule[displayed_day][i]["checked"] == True:
            return("x")
        else:
            return(" ")

    i: int = 0
    while i < len(schedule_days):
        print(f"{i + 1}. [{check()}] {schedule[displayed_day][i]['task']}")     # i + 1 so we don't state "0"
        i += 1

    # now person inputs "1" and makes checked false
    checkstatus = int(input("Would you like to check / uncheck something?: "))

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
    