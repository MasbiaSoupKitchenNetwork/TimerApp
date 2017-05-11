# Timer App

This terminal app used to help the folks at the Masbia Soup Kitchen Network assess the efficiency of the process they use to provide for their clients.

Once the program is installed, it will create files in the same folder the program is run from. Data is saved after every timed event, so no reason to stress if you accidentally close the program. <br />

<a href="https://asciinema.org/a/9ui1ugfhh0g3mov675pewdh6k" target="_blank"><img src="https://asciinema.org/a/9ui1ugfhh0g3mov675pewdh6k.png" /></a> <br />

## Installation
Download <code>timed_event.py</code> and <code>menu.py</code> to the folder you would like to store both your data and the program in.

## Use
Use your favorate terminal program to navigate into the directory where you have downloaded <code>timed_event.py</code> and <code>menu.py</code> and run <code>python menu.py</code>. <br />
You will see... <br />
![Your menu options](https://github.com/MasbiaSoupKitchenNetwork/TimerApp/blob/master/menu_preview_image.png) <br />
Once you select an event to time from the menu, you will begin timing. To stop the timer, hit spacebar. The event will save and the program will print to the screen all the start and end times and elasped times that have been recorded for that event. <br />
In this example, a client managed to fill out your form in one second! <br />
![Example data saved for one entry. Your task took just one second!](https://github.com/MasbiaSoupKitchenNetwork/TimerApp/blob/master/one_entry_preview_image.png) <br />
Hitting any key will bring you back to the menu and you may begin timing the next event.
You may exit the program from the menu or any time with <code>ctrl+c</code>. If you use <code>ctrl+c</code> to exit while a event is bring timed, you will stop recording without saving and return to the menu.

## Troubleshooting
### Version
This program is written in Python 3. If you have only Python 2, as is still default on macs, you'll need to download and run the program with Python 3.
### Stop accidental recordings
If you begin recording an event accidentially, you can stop without saving by hitting <code>ctrl+c</code>, which will stop the recording and return to the menu.
