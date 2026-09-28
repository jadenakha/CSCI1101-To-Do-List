from submodule import defaultsettings
# defaultsettings.settingsmenu()

def taskchecking(printDays, schedule, schedule_days, printToday, togglePrints):
    checkstatus = str(input("What day would you like to edit the tasks in (caps sensitive, like 'Monday')? Type 'exit' to return back to options: "))

    if checkstatus not in schedule_days or checkstatus == "exit":
        print("Day not in Schedule Days! Check caps!")
        defaultsettings.settingsmenu(printDays, schedule, schedule_days, printToday, togglePrints)

    def statuscheck():                                               # [checkstatus - 1] because we don't want the possibility of "0"
        if schedule[checkstatus][modifyCheck - 1]["checked"] == True:
            schedule[checkstatus][modifyCheck - 1]["checked"] = False
            print("Unchecked!")
        else:
            schedule[checkstatus][modifyCheck - 1]["checked"] = True
            print("Checked!")

    try:
        modifyCheck = int(input("What task would you like to check or uncheck from that day? "))
        if modifyCheck > 0 and modifyCheck <= len(schedule[checkstatus]):         # if it's not 0 (expect 1 and above) and less than or = to length (1 minimum, also bounds)
            statuscheck()
        else:
            raise IndexError
    except IndexError:
        print("Not a valid task #")
        print()
        defaultsettings.settingsmenu(printDays, schedule, schedule_days, printToday, togglePrints)

