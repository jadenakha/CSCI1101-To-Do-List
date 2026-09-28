from submodule import defaultsettings
# defaultsettings.settingsmenu()


def addtoday(schedule):
    addnew = str(input("To what day would you like to add (caps sensitive, like 'Monday')? Type 'exit' to return back to options: "))

    if addnew == "exit":
        # x = str(input("What would you like to try and do? Available: 'Add' or 'Check' to check something off?"))
        defaultsettings.settingsmenu()
    else:
        taskName = str(input(f"What task would you like to add for {addnew}?: "))
        try:
            schedule[addnew].append({"task": taskName, "checked": False})
        except IndexError:
            print("No day exists to add onto! Days are caps-sensitive. Try something like 'Monday'")
            print()
            defaultsettings.settingsmenu()
