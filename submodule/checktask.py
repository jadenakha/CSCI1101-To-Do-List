from submodule import defaultsettings
# defaultsettings.settingsmenu()

def taskchecking():
    clearconsole()
    checkstatus = input("Would you like to check / uncheck something? Type 'exit' to return back to options: ")
    if checkstatus == "exit":
        # x = str(input("What would you like to try and do? Available: 'Add' or 'Check' to check something off?"))
        defaultsettings.settingsmenu()

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
