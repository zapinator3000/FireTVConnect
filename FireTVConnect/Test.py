input("Press Enter")
import FireTVConnect as firetv
import sys
tv=firetv.Connector("192.168.1.73")
tv.Reset()
tv.Connect()
try:
    while True:
        tv.KeyEvent("Play/Pause")
        input("Press Enter to play/pause")
finally:
    tv.Reset()
    sys.exit(0)
