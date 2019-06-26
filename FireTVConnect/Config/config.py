#!/usr/bin/python
#This is the Configuration system for the New "Live" Game Console
import os
import time
import re, sys

class configurator:
    def __init__(self,configfile):
        self.config_file=configfile
        self.values=[]
        self.keys=[]
    def process(self):
        print("Reading Configuration...")
        config=re.split(r"\n", open(self.config_file,"r").read())
        for item in config:
            if item!="" or item!="\n" or item!=" ":
                try:
                    if not item[0]=="#":
                        splits=item.split("=",1)
                    #print("Keys: "+str(splits[0]))
                    #print("value: "+str(splits[1]))
                        self.values.append(splits[1])
                        self.keys.append(splits[0])
                except:
                    if not "#" in item:
                        try:
                            print("Problem parsing config file, using backup add mode...")
                            splits=item.split("=",1)
                            self.values.append(splits[1])
                            self.keys.append(splits[0])
                            print("OK!")
                        except:
                            print("There was an issue parsing the config file")
                            sys.exit(1)
        return self.keys,self.values
