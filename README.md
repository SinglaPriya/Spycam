# Spycam
Click a picture of anyone who tries to login into your computer.

Pre-requisities:
-Python 3.6

Changes in batch file:
-Download the batch file (.bat) and python file in C drive.
-Right click on batch file and choose Edit.
-Change the path of the python executable. But almost always you will find it in "C:\Users\%User_name%\AppData\Local\Programs\Python\Python_version\python.exe"
-Change the path of Python file to where you have downloaded.

This python script (cam.py) will save the images in D drive of your machine. You can change it as per your requirements too.

Use cases:
1. If you want to click the picture of the person as soon as your system boots up:
     - create shortcut of the batch file (trigger.bat).
     - Press Windows+R and type shell:startup, or open 'C:\Users\priya\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.
     - Paste the shortcut in the Startup folder.

2. If you want to click the picture as soon as someone Logson:
    - Open Task Scheduler and click on 'Create Task'.
    - A Create Task windows will be opened.
    - Under the General section, Name your task and click on Next.
    -Under the Trigger section, select New and a new Trigger windows will be opened.
    - Select 'At log on' from drop down menu for Begin the Task.
    - Select 'Any User' and click OK.
    - Under the Action section, select 'New'. 'New Action' windows will be opened. 
    - Select 'Start a Program' from drop down menu for Action.
    - Click on Browse and locate the batch file on your computer and click OK.
    -Under the Conditions Section, unselect the 'Stop if computer switches to batter power' and 'Start the task only if the computer is on AC power'
  - Click on Ok and a new task will be created.

3. If you want to click the picture when someone is on the Windows Logon page:
    - Open Task Scheduler and click on 'Create Task'.
    - A Create Task windows will be opened.
    - Under the General section, Name your task and click on Next.
    -Under the Trigger section, select New and a new Trigger windows will be opened.
    - Select 'On an event' from drop down menu for Begin the Task.
    - Select 'Microsoft-Windows-Authentication User Interface/Operational' from dropdown menu for Log and 'Authentication User Interface' from dropdown menu for Source and click OK.
    - Under the Action section, select 'New'. 'New Action' windows will be opened. 
    - Select 'Start a Program' from drop down menu for Action.
    - Click on Browse and locate the batch file on your computer and click OK.
    -Under the Conditions Section, unselect the 'Stop if computer switches to batter power' and 'Start the task only if the computer is on AC power'
  - Click on Ok and a new task will be created.

You can explore many options under Task Scheduler and trigger the batch file for many events and actions.
