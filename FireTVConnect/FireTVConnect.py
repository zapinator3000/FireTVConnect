""" Title: FireTV Connect
    Author: Zackery Painter
    Date Created: 6/16/2019
    Date Modified: 6/16/2019

    Description: This module gives the ability to connect to and control a FireTV or FireTV Stick using an ADB Connection

    Objects:
            debugger:
                    alert
            adb:
                    SendCMD
            Connector:
                    Connect
                    KeyEvent
                    Reset


"""
import os, time, sys, subprocess
from datetime import datetime


"""Debugger Class: Creates a DEBUGGING object for logging and standard alerts

Functions:
  Alert:
      Shows a debugging message with a time stamp.

      Alert Types:
          Alert: Give a standard error message with DEBUG Title
          Sub_alert: Give a sub-alert message with additional information of the previous DEBUG message

"""
class debugger:
    def __init__(self):
        pass
    def alert(self,content,typ):
        now=datetime.now()
        if typ=="Alert":
            print(str(now.strftime("%H:%M:%S"))+" : DEBUG: "+str(content))
        elif typ=="Sub_alert":
            print(str(now.strftime("%H:%M:%S"))+" :         "+str(content))
"""ADB Class:
        Communicates with the ADB server
Functions:
  SendCMD(command):
      Send a command to the fire stick using the ADB connection passed ot the object
      

"""
class adb:
    def __init__(self):
        self.adb_loc="adb"
    def SendCMD(self,command):
        cmd_res=subprocess.call(str(self.adb_loc)+" "+str(command),stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return cmd_res
"""Connector Class(ip_address,port):
        This is the main class to be created by the importing script
            port: Sets the Port
            ip_address: Sets the address to connect to
    Connect:
        Connects to the address and port as defined in the calling object
    KeyEvent(event):
        Creates and sends a Key Event to the FireTV using the built-in Library (Emulating a Remote)
        event: The input event to call, can be anything below:
                Up
                Down
                Left
                Right
                Enter
                Back
                Home
                Menu
                Play/Pause
                Previous
                Next
    Reset:
        Resets the ADB server by disconnecting any connections to ADB and killing the old server.
"""
class Connector:
    debug=False # Change this to True to enable debugging
    silent=False \
    KeyLibrary={"Up" : "19","Down" : "20","Left":"21","Right":"22","Enter":"66","Back":"4","Home":"3","Menu":"1","Play/Pause":"85","Previous":"88","Next":"87"}
    if debug==True: # If enabled by default, create a debug object
        db=debugger()
    if debug==True:
        db.alert("Creating adb object","Alert")
    adbclient=adb()
    if debug==True:
        db.alert("Created ADB object:","Alert")
        db.alert("Object info: "+str(adb),"Sub_alert")
    def __init__(self,ip_address,port=5555):
        self.ip_address=ip_address # Set the ip_address and port to the input values
        self.port=port
        if Connector.debug==True:
            self.db.alert("Created Connector Object:","Alert")
            self.db.alert(self,"Sub_alert")
            self.db.alert("Address: "+str(ip_address),"Sub_alert")
            self.db.alert("Port: "+str(port),"Sub_alert")
    def Connect(self):

        if Connector.debug==True:
            self.db.alert("Attempting to connect...","Alert")
            self.db.alert("Connecting to: "+str(self.ip_address)+":"+str(self.port),"Sub_alert")
        elif Connector.silent==False:
            print("Connecting to FireTv")
        cmd_res=self.adbclient.SendCMD("connect "+str(self.ip_address)+":"+str(self.port)) # Send a connect command using the adb client
        if not cmd_res==0: # If it returns anything but 0, give a warning about being unable to connect
            print("Unable to Connect to FireTV, am I on?")

        elif Connector.debug==True: # If the debugging is true, show debugging info
            self.db.alert("Connected FireTv from object with following information: ","Alert")
            self.db.alert("Address: "+str(self.ip_address),"Sub_alert")
            self.db.alert("Port: "+str(self.port),"Sub_alert")
        elif Connector.silent==False: # If not in silent mode, print connected
            print("Connected To FireTV!")
    def KeyEvent(self,event):
        if Connector.debug==True: # Give debugging information
            self.db.alert("Creating Key Event: ","Alert")
            self.db.alert("KeyEvent: "+str(event),"Sub_alert")
            self.db.alert("KeyCode: "+str(self.KeyLibrary[str(event)]),"Sub_alert")
        cmd_res=self.adbclient.SendCMD("shell input keyevent "+str(self.KeyLibrary[str(event)])) # Send a keyboard input event using the adb 
        if cmd_res==0:
            if Connector.debug==True:
                self.db.alert("Key Event Send Status: Sent (Success!)","Sub_alert")
            elif Connector.silent==False:
                print("KeyEvent has been sent")
        else:
            if Connector.debug==False:
                print("Unable to Send Key Event!")
                input("Press Enter to Exit")
                sys.exit(1)
            else:
                self.db.alert("Key Event Send Status: Unable to Send(FAIL)","Sub_alert")
    def Reset(self): 
        if Connector.debug==True:
            self.db.alert("Resetting adb server...","Alert")
        cmd_res=self.adbclient.SendCMD("disconnect") # Disconnect the current connection
        if not cmd_res==0:
            print("Unable to Reset Server: Disconnect Failed!")
            if Connector.debug==False:
                input("Press Enter to Exit")
                sys.exit(1)
        cmd_res=self.adbclient.SendCMD("kill-server") # Killoff the server
        if not cmd_res==0:
            print("Unable to Reset Server: Unable to Kill Server!")
            if Connector.debug==False:
                input("Press Enter to Exit")
                sys.exit(1)
        else:
            if Connector.debug==True:
                self.db.alert("Server has been Reset","Sub_alert")
    
    def LaunchApp(self,name,cmd):
        if Connector.debug==True:
            self.db.alert("Launching the following app: ","Alert")
            self.db.alert("App Name: "+str(name),"Sub_alert")
            self.db.alert("App Launch Point: "+str(cmd),"Sub_alert")
        elif Connector.silent==False:
            print("Launching app: "+str(name))
        cmd_res=self.adbclient.SendCMD("shell monkey -p "+str(cmd)+" -c android.intent.category.LAUNCHER 1") #Launch the given app
        if cmd_res==0:
            if Connector.debug==True:
                self.db.alert("Launch App Send Status: Sent (Success!)","Sub_alert")
            elif Connector.silent==False:
                print("App has been Launched")
        else:
            if Connector.debug==False:
                print("Unable to Send Launch App!")
                input("Press Enter to Exit")
                sys.exit(1)
            else:
                self.db.alert("Launch App Send Status: Unable to Send(FAIL)","Sub_alert")
            
