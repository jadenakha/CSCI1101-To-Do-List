make sure you

git add "(file path)" (you might have to do this for every file you add, i just git add the entire project folder again)
git commit -m "any message"
git push -u origin main

to keep track of your work
https://github.com/jadenakha/CSCI1101-To-Do-List/tree/main

--

# project map

1. start from main.py
import the following from "submodule" folder (https://stackoverflow.com/questions/8953844/import-module-from-subfolder)

-- 

from submodule import addtask
# addtask.addtoday()
from submodule import defaultsettings
# defaultsettings.settingsmenu()
from submodule import checktask
# checktask.taskchecking()

--



--

how to clear consoles:

# Source - https://stackoverflow.com/a/2084628
# Posted by poke, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-23, License - CC BY-SA 3.0

import os
def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')

then just call "clearconsole()"
