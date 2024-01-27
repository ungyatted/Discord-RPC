 # Code Made by ungyatted.
 # If you come up with any errors, dont forget to contact me on discord.

 # BEFORE YOU START MAKE SURE TO USE
 # pip install pypresence

from pypresence import Presence
import time
# To clientID make sure you put your Bot's application id.
RPC = Presence("clientID")
RPC.connect()

print("You should have your RPC on now.")

while True:
    RPC.update(
        large_image="icon", # put here the name that you uploaded the picture with.
        large_text="ungyatted", # replace it with whatever you want as your larger picture's image.
        small_image="smallicon", # put here the name that you uploaded the secondary picture with.
        small_text="discord.gg/", # replace it with whatever you want as your smaller picture's image.
        details="Message me if you need", # replace this with your message that you want to be displayed.
        state= "Help related to codes.", # replace this with your message that you want to be displayed on the second line.
        start= int(time.time()),
        buttons= [{"label": "firsturl", "url": "https://www.firsturl.com"},{"label": "secondurl","url": "https://www.secondurl.com"}] # replace "firsturl" and "secondurl" with whatever you want, and also replace the links too.
                        )
    
    time.sleep(70)