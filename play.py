# The Musical Hosting Site
# Author: thackeraaron

# References:
# https://automatetheboringstuff.com/chapter18/

# The hosting site (This is not my site):
# https://eternalweb.uk/whmcs/index.php
# https://web.archive.org/web/20200814002519/https://eternalweb.uk/whmcs/index.php

import pyautogui, sys, time

# This uses a clipped version of the full image. speed > accuracy.
speedDetect = True

# This holds what the notes are (disclaimer: I know nothing about music)
# Its in relation to the notes on the site (left to right, 0 to 3)
noteOrder = ['C', 'D', 'E', 'F']

# The interval between notes
sleepSpeed = 0.0025

# This function of spaghetti code finds the note coordinates
# returns an array of tuples with the coordinates
def findNotes():
	a = pyautogui.locateOnScreen('a.png' if not speedDetect else 'speed_a.png')
	if a == None:
		print("Cannot Find A")
		sys.exit(1)
	else:
		print("Found A")
	ax = a.left + (a.width//2)
	ay = a.top + (a.height//2)

	b = pyautogui.locateOnScreen('b.png' if not speedDetect else 'speed_b.png')
	if b == None:
		print("Cannot Find B")
		sys.exit(1)
	else:
		print("Found B")
	bx = b.left + (b.width//2)
	by = b.top + (b.height//2)

	c = pyautogui.locateOnScreen('c.png' if not speedDetect else 'speed_c.png')
	if c == None:
		print("Cannot Find C")
		sys.exit(1)
	else:
		print("Found C")
	cx = c.left + (c.width//2)
	cy = c.top + (c.height//2)

	d = pyautogui.locateOnScreen('d.png' if not speedDetect else 'speed_d.png')
	if d == None:
		print("Cannot Find D")
		sys.exit(1)
	else:
		print("Found D")
	dx = d.left + (d.width//2)
	dy = d.top + (d.height//2)

	return [(ax, ay), (bx, by), (cx, cy), (dx, dy)]

# This moves the mouse to the note based off the given note
def playNote(notes, i):
	global sleepSpeed
	pyautogui.moveTo(notes[i][0], notes[i][1])
	time.sleep(sleepSpeed)
	pyautogui.moveTo(1, 1)

# This parses the note
def parseNote(notes, note):
	global noteOrder
	print("doing %s" % note)
	if(note==noteOrder[0]):
		playNote(notes, 0)
		return
	elif(note==noteOrder[1]):
		playNote(notes, 1)
		return
	elif(note==noteOrder[2]):
		playNote(notes, 2)
		return
	elif(note==noteOrder[3]):
		playNote(notes, 3)
		return
	else: # This is a space so we must sleep
		global sleepSpeed
		time.sleep(sleepSpeed*20) # multiplied because not a note
		return

# This plays the song
# takes an array of coordinates and a string "CDEF CDEF CDEF" for example based on the noteOrder array
def play(notes, song):
	global sleepSpeed
	for note in song:
		parseNote(notes, note)
		time.sleep(sleepSpeed)



# This holds the positions of the notes
notes = findNotes()

# Mary had a little lamb
song = "EDCDEEE   DDD   EFF  EDCDEEE  EDDEDC"
play(notes, song)
