# FireTVConnect
This is a python library for connecting to and controlling a fire TV 

Installation:
Windows:

1. Place the contents of the entire directory into the same folder that your script is in.
 (I don't know how to do the easy install stuff yet, or setup.py... If anyone wants to do that for me, go ahead)

Linux:
1. Install adb according to your distribution. It may be packaged under another name. There is a lot of documentation for this online already.
2. Download this using wget or git. 
3. Copy the entire contents to your program's root directory. (Again, I don't know how to set up an easy installer yet and I don't have to do so right now. Feel free to re-package as one.)

Usage:
  import the software as follows:
  
    import FireTVConnect as firetv
    
 For more Usage information, see the test.py script.
 
Configuration:
  The main configuration file is in:
       [FireTVConnectDirectory]/Config/FireTV.config
  There are a few options that can be configured.
     
     DEBUG - Setting this True Enables the DEBUG mode
     SILENT - Setting this to True prevents normal alerts 
 
Note:

  This module requires adb and contains third-party applications. Please see the adb lisences and notices enclosed and on the Android developer website.

Additional Notes:

  You will need to know the IP address of your Fire-TV/Fire-TV Stick. See Amazon's support page for information on how to find this. You will also need to have USB Debugging enabled on your FireTV, see Amazon's support page on how to do this.

Requirements:

Windows 7/8/8.1/10, Maybe Linux (Untested), Maybe Unix (Untested).

Python 3.6 (Not compatible with 2.7 or 3.7 because of Pyaudio, but only for voice test program)

