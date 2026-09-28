from submodule import defaultsettings
# defaultsettings.settingsmenu()

def taskchecking(schedule):
    checkstatus = str(input("What day would you like to edit the tasks in (caps sensitive, like 'Monday')? Type 'exit' to return back to options: "))

    
    if checkstatus == "exit":
        # x = str(input("What would you like to try and do? Available: 'Add' or 'Check' to check something off?"))
        defaultsettings.settingsmenu()

    modifyCheck = int(input("What task would you like to check or uncheck from that day? "))

    def statuscheck():                                               # [checkstatus - 1] because we don't want the possibility of "0"
        if schedule[checkstatus][modifyCheck - 1]["checked"] == True:
            schedule[checkstatus][modifyCheck - 1]["checked"] = False
            print("Unchecked!")
        else:
            schedule[checkstatus][modifyCheck - 1]["checked"] = True
            print("Checked!")

    if modifyCheck > 0 and modifyCheck <= len(schedule[checkstatus]):         # if it's not 0 (expect 1 and above) and less than or = to length (1 minimum, also bounds)
        statuscheck()
    else:
        print("Doesn't Exist")
