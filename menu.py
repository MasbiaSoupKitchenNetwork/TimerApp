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

def ask_if_want_to_leave():
	print "Exit (y/n): "
	ready_to_leave = readchar.readchar()
	if ready_to_leave == "y" or ready_to_leave == "Y":
		print "You're about about leave"
		exit()

while (True):
	options = menu.keys()
	options.sort() # since keys don't have an order, we order them
	print chr(27) + "[2J" # clears screen so can see menu better
	for entry in options:
		print entry, menu[entry]
	print "Please enter your selection: "
	selection = readchar.readchar()
	if selection == "\x03" or selection == "\x04" or selection == "\x05": # cmd+d twice to select all
		ask_if_want_to_leave()
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
		ask_if_want_to_leave()
	else: 
		print "Please select press any key and then select 1-4"
	