from submodule import defaultsettings
# defaultsettings.settingsmenu()


def addtoday(printDays, schedule, schedule_days, printToday, togglePrints):
    addnew = str(input("To what day would you like to add (caps sensitive, like 'Monday')? Type 'exit' to return back to options: "))

    if addnew not in schedule_days or addnew == "exit": # Checks if its a valid typed day
        defaultsettings.settingsmenu(printDays, schedule, schedule_days, printToday, togglePrints)

    taskName = str(input(f"What task would you like to add for {addnew}?: "))
    try:
        schedule[addnew].append({"task": taskName, "checked": False}) # Appends
    except: # If there's any error notify in case something is bad with something but doesnt break app here 
        print("Error?")
        print()
        defaultsettings.settingsmenu(printDays, schedule, schedule_days, printToday, togglePrints)
