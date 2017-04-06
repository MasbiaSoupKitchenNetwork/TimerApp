import readchar
import time

## global vars like being on top ##
is_counting = False
start_count = 0

def counting_true():
    global start_count
    start_count = time.time()
    print "I've started counting"

def counting_false():
    end_count = time.time()
    print "I've stopped counting"
    elapsed_time = int(end_count - start_count)
    print "The elapsed time is " + str(elapsed_time) + " seconds"

def toggle_counting():
    global is_counting
    is_counting = not is_counting
    if is_counting == True:
        counting_true()
    else:
        counting_false()

while (True):
    saved_char = readchar.readchar()
    if saved_char == "\x03" or saved_char == "\x04" or saved_char == "\x05":
        break
    if saved_char != " ":
        print "You didn't press space, you pressed: " + saved_char
    else:
        print "You hit the space" 
        toggle_counting()


