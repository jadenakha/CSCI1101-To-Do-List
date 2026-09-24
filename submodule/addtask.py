from submodule import defaultsettings
# defaultsettings.settingsmenu()


def addtoday():
    clearconsole()
    addnew = str(input("What would you like to add? Type 'exit' to return back to options: "))

    if addnew == "exit":
        # x = str(input("What would you like to try and do? Available: 'Add' or 'Check' to check something off?"))
        defaultsettings.settingsmenu()
    else:
        schedule[displayed_day].append({"task": addnew, "checked": False})
