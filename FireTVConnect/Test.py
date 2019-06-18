""" File Name: Test.py
    Creator: Zackery Painter
    Date Created: 6/16/2019
    Date Modified: 6/17/2019
    Description: This is a test program for the FireTVConnect module. 
"""

import FireTVConnect as firetv # Import the FireTVConnector
import sys # Import sys module
# Create a fire tv connector address
tv=firetv.Connector("IP ADDRESS") # Put in your FireTV's address here. 
tv.Reset() # Reset and clean up any previous processes 
tv.Connect() # Connect to the FireTV
try:
    while True:
        tv.KeyEvent("Play/Pause") # Send the key event to Play or Pause
        input("Press Enter to play/pause")
finally:
    tv.Reset() # Disconnect and kill the server
    sys.exit(0)
