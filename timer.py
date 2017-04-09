import readchar
import time
import yaml
import os

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

def save_data(elapsed_time, form_time_sec_filepath):
    if os.path.exists(form_time_sec_filepath):
        append_write = "a+" # append if already exists
    else:
        append_write = "w+" # make a new file if it doesn't exist
    with open(form_time_sec_filepath, append_write) as form_time_sec_file:
        form_time_sec_file.write(str(elapsed_time) + "\n")
        form_time_sec_file.seek(0) # move file cursor from the end of the file to the beginning so we can read it
        print form_time_sec_file.read()

while (True):
    saved_char = readchar.readchar()
    if saved_char == "\x03" or saved_char == "\x04" or saved_char == "\x05":
        save_data()
        break
    if saved_char != " ":
        print "You didn't press space, you pressed: " + saved_char
    else:
        print "You hit the space" 
        toggle_counting()


