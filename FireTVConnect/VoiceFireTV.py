import os
import time, sys
import speech_recognition as sr
import FireTVConnect as firetv
tv=firetv.Connector("IP ADDRESS HERE")
tv.Reset()
tv.Connect()
#This is the example code from the Speech Recognition module
def callback(recognizer, audio):
    try:
        transcribed = recognizer.recognize_google(audio)
        print("Transcribed as: " + transcribed)
        if transcribed=="goodbye":
            sys.exit(0)
        if "pause" in transcribed or "play" in transcribed or "resume" in transcribed:
            tv.KeyEvent("Play/Pause")
        if "home" in transcribed:
            tv.KeyEvent("Home")
        if "Hulu" in transcribed:
            tv.LaunchApp("Hulu","com.hulu.plus")
        if "enter" in transcribed or "select" in transcribed:
            tv.KeyEvent("Enter")
        if "YouTube" in transcribed:
            tv.LaunchApp("YouTube","org.chromium.youtube_apk")
        if "Netflix" in transcribed:
            tv.LaunchApp("Netflix","com.netflix.ninja")
        if "right" in transcribed:
            tv.KeyEvent("Right")
        if "left" in transcribed:
            tv.KeyEvent("Left")
    except sr.UnknownValueError:pass

    except sr.RequestError:
        print("Fatal Error")

print("Please wait...")
# obtain audio from the microphone
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)
print("Ready for commands: ")
stop_listening = r.listen_in_background(m, callback)
try:
    while True: pass
finally:
    tv.Reset()
