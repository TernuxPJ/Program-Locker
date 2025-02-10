**Program Blocker**

A simple Python application that allows you to block specific programs from running on your system using `tkinter` for the GUI and `psutil` for process management.

**Features**

Block any program by name.

Runs in the background and continuously monitors for blocked programs.

User-friendly GUI built with tkinter.

**Requirements**

Make sure you have the following dependencies installed:

```

pip install psutil

```


**How to Use**

Run the script:

python script.py **or** python Program_Blocker.py

Enter the name of the program you want to block (e.g., notepad.exe).

Click "Start Blocking" to prevent the program from running.

The program will terminate any instance of the blocked program.

Click "Exit" to close the application.

**Notes**

Program names should be entered exactly as they appear in Task Manager (case-insensitive).

The script runs in the background using a separate thread to monitor processes.

You need to run the script with administrative privileges to block system applications.
