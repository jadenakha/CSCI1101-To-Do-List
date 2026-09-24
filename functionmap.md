how to clear consoles:

# Source - https://stackoverflow.com/a/2084628
# Posted by poke, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-23, License - CC BY-SA 3.0

import os
def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')

then just call "clearconsole()"

--

