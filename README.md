# Black-White-png
looks at decent color pictures and draws ugly black-white pictures

How to install:

Make sure your computer has a command line app. Mac and Linux systems should already have one, and Windows users should install WSL using these instructions: https://docs.microsoft.com/en-us/windows/wsl/install-win10

Install Python 3 on your computer and make sure that your command line app recognizes the "python3" and "pip" commands.

Enter "pip install png" in your command line app.

Download the black-white-png.py file from this Github project.



How to use:

Put a .png file and a copy of black-white-png.py in the same folder.

Open your command line app and use the "cd" command so that folder becomes your working directory.

Enter "python3 black-white-png.py <brightness> <in file name> <out file name>".

Brightness can be any integer between 0 and 256 (exclusive)\*. Every pixel becomes black if its brightness is less than the brightness you entered.

Example: The command "python3 black-white-png.py 128 gate.png gate128.png" creates a file named gate128.png. In that file, every pixel is black if its brightness was less than 128 in gate.png.

\*Technically it will work with any integer, but integers 0 or less will simply result in a white rectangle, and integers 256 or greater will simply result in a black rectangle.