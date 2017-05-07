import readchar
from timed_event import TimedEvent

form_filling = TimedEvent("form_filling")
food_grabbing = TimedEvent("food_grabbing")

while (True): # True always
    if food_grabbing.is_counting is False: # instance var that is False when not timing, True when timing
        print "You can start timing by hitting space"
    saved_char = readchar.readchar()
    if saved_char == "\x03" or saved_char == "\x04" or saved_char == "\x05":
        break # break when you press ctl+C, ctl+D, ctl+Z
    if saved_char != " ":
        print "You didn't press space, you pressed: " + saved_char # if you press not-space, it reminds you to press space and tells you it hasn't stopped/started recording
    else:
        food_grabbing.toggle_counting()


