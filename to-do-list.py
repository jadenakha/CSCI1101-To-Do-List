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

# soon to become function
# while True:
# print(f"== {schedule[day]} ==")
print(f"== {schedule_days[0]} ==")
displayed_day: str = schedule_days[0]

# iterate through all lists
i: int = 0
while i < len(schedule_days):
    print(schedule[displayed_day][i])
    i += 1
