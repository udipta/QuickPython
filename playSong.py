#!/usr/bin/python3
import os
import random

def track(song):
	os.chdir('/home/udipta/Music/')
	msg = 'mpg321 -q '+ random.choice(song)
	os.system(msg)

def readFile(filename):
        with open(filename, 'r+') as f:
                temp = f.read().splitlines()
                return temp

List = readFile('music')
track(List)
