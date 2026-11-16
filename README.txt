PLATFORMPRO - CP-049 (MULTI-FILE VERSION)

FILES
-----
main.py                 Run the program from this file.
config.py               Stores the JSON filename and default settings.
time_utils.py           Time conversion and time input functions.
storage.py              Saves and loads train records.
train_manager.py        Register, search, and view trains.
platform_calculator.py  Calculates the minimum simultaneous platforms.
allocation.py            Assigns trains to reserved/general platforms.
delay_manager.py         Updates delayed train schedules and reallocates.
reports.py               Platform chart, reserved settings, utilisation.

HOW TO RUN IN VS CODE
---------------------
1. Extract the ZIP file.
2. Open the extracted PlatformPro_MultiFile folder in VS Code.
3. Open Terminal > New Terminal.
4. Run: python main.py
   If that does not work on Windows, run: py main.py

IMPORTANT
---------
Keep all .py files in the same folder.
Run main.py only. Do not run each module separately.
The program creates platformpro_data.json automatically in this folder.
Existing data in an older platformpro_data.json can be loaded if you copy
that file into this folder. Both HH:MM text times and minute-number times
are supported.

TEST FOR MINIMUM PLATFORMS
--------------------------
Register:
T101 09:00-10:30
T102 09:15-11:00
T103 10:00-11:30
T104 11:30-12:00

The minimum is 3 because three trains overlap between 10:00 and 10:30.