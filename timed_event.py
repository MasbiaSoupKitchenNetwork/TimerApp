import readchar
import time
import yaml
import os
import sys

class TimedEvent():

    def __init__(self, activity="form_filling"):
        self.is_counting = False # each boolean is named after a question bc than its value is clear
        self.start_time = 0
        self.activity = activity


    def start_counting(self):
        self.start_time = time.time()
        print "I've started counting. Press esc to cancel the counting. Spacebar stops and records the count."
        while (True): # True always
            saved_char = readchar.readchar()
            if saved_char == "\x03" or saved_char == "\x04" or saved_char == "\x05":
                sys.exit() # when you press ctl+C, ctl+D, ctl+Z 
            if saved_char == "\x1b":
                break # ESC
            if saved_char != " ":
                print "You didn't press space, you pressed: " + saved_char # if you press not-space, it reminds you to press space and tells you it hasn't stopped/started recording
            else:
                self.stop_counting()
                readchar.readchar() # halts the clearing of the screen until a selection is entered so the selection is printed 
                break

    def stop_counting(self):
        end_time = time.time() # gives float
        print "I've stopped counting"
        elapsed_time = int(end_time - self.start_time)
        print "The elapsed time is " + str(elapsed_time) + " seconds"
        self.save_data_to_yaml_file(end_time, elapsed_time)


    def save_data_to_yaml_file(self, end_time, elapsed_time):
        """
        We decided that the the file path would be the same as the activity name.
        Please don't cry when debugging later.
        """
        filepath = self.activity
        print "elapsed_time is: " + str(elapsed_time)
        print "filepath is: " + filepath
        result = {
            "start_time" : self.start_time,
            "end_time" : end_time,
            "elapsed_time" : elapsed_time,
            "activity" : self.activity
        }
        
        if os.path.exists(filepath):
            read_write = "r+" # read write if already exists
        else:
            read_write = "w+" # make a new file if it doesn't exist
        with open(filepath, read_write) as file:
            file_data = file.read()
            file.seek(0) #  move cursor back to the top to overwrite our things
            if file_data == "":
                previous_data = []
            else:
                previous_data = yaml.load(file_data)
            # extending list
            new_data = previous_data + [result]
            file.write(yaml.dump(new_data))
            file.seek(0) # move file cursor from the end of the file to the beginning so we can read it
            print file.read()




