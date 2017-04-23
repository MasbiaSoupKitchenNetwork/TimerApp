import readchar
import time
import yaml
import os

# function signature is the properties from the arguments (how many?, what type?, what order?)

## global vars like being on top ##
is_counting = False # each boolean is named after a question bc than its value is clear
start_time = 0
activity = "form_filling"

def start_counting():
    global start_time
    start_time = time.time()
    print "I've started counting"

def stop_counting():
    end_time = time.time() # gives float
    print "I've stopped counting"
    elapsed_time = int(end_time - start_time)
    print "The elapsed time is " + str(elapsed_time) + " seconds"
    save_data_to_yaml_file(start_time, end_time, elapsed_time, "fill_forms_time")

def toggle_counting():
    global is_counting
    if is_counting:
        stop_counting()
    else:
        start_counting()
    is_counting = not is_counting


def save_data_to_file(start_time, end_time, elapsed_time, filepath): # arg names should make type obvious
    if os.path.exists(filepath):
        append_write = "a+" # append if already exists
    else:
        append_write = "w+" # make a new file if it doesn't exist
    with open(filepath, append_write) as file:
        file.write(str(elapsed_time) + "\n")
        file.seek(0) # move file cursor from the end of the file to the beginning so we can read it
        print file.read()


def save_data_to_yaml_file(start_time, end_time, elapsed_time, filepath): 
    print "elapsed_time is: " + str(elapsed_time)
    print "filepath is: " + filepath
    result = {
        "start_time" : start_time,
        "end_time" : end_time,
        "elapsed_time" : elapsed_time,
        "activity" : activity
    }
    
    if os.path.exists(filepath):
        read_write = "r+" # read write if already exists
    else:
        read_write = "w+" # make a new file if it doesn't exist
    with open(filepath, read_write) as file:
        file_data = file.read()
        file.seek(0)
        if file_data == "":
            previous_data = []
        else:
            print "file_data: " + file_data
            previous_data = yaml.load(file_data)
        # extending object
        new_data = previous_data + [result]
        file.write(yaml.dump(new_data))
        file.seek(0) # move file cursor from the end of the file to the beginning so we can read it
        print file.read()





while (True): # True always
    if is_counting is False: # global var that is False when not timing, True when timing
        print "You can start timing by hitting space"
    saved_char = readchar.readchar()
    if saved_char == "\x03" or saved_char == "\x04" or saved_char == "\x05":
        break # break when you press ctl+C, ctl+D, ctl+Z
    if saved_char != " ":
        print "You didn't press space, you pressed: " + saved_char # if you press not-space, it reminds you to press space and tells you it hasn't stopped/started recording
    else:
        toggle_counting()


