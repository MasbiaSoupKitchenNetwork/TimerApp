import readchar
from timed_event import TimedEvent

## define menu option ##
menu = {}
menu['1']="Time form filling" 
menu['2']="Time food grabbing"
menu['3']="Time food loading"
menu['4']="Exit"

## create instances of each possible timed event ##
form_filling = TimedEvent("form_filling")
food_grabbing = TimedEvent("food_grabbing")
food_loading = TimedEvent("food_loading")

while (True):
	options = menu.keys()
	options.sort() # since keys don't have an order, we order them
	print chr(27) + "[2J" # clears screen so can see menu better
	for entry in options:
		print entry, menu[entry]
	print "Please enter your selection: "
	selection = readchar.readchar()
	if selection == "\x03" or selection == "\x04" or selection == "\x05": # cmd+d twice to select all
		break
	if selection == "1":
		print "Time form filling"
		form_filling.start_counting()
	elif selection == "2":
		print "Time food grabbing"
		food_grabbing.start_counting()
	elif selection == "3":
		print "Time for food loading"
		food_loading.start_counting()
	elif selection == "4":
		print "You're about about leave"
		break
	else: 
		print "Please select press any key and then select 1-4"
	readchar.readchar() # halts the clearing of the screen until a selection is entered so the selection is printed 
