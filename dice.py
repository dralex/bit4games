# -----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# bit4games collection
#
# Dice program
#
# Author: Alexey Fedoseev <aleksey@fedoseev.net>, 2019
# -----------------------------------------------------------------------------

import microbit as m
import random
import music

random.seed(m.accelerometer.get_x())

dices = (2, 3, 4, 6, 8, 10, 12, 20, 100)
dice = 3 # index
result = None

def update_display():
	if not result:
		m.display.scroll('d' + str(dices[dice]), wait=False, loop=True)
		music.play(music.POWER_UP)
	else:
		if result < 10:
			m.display.show(result)
		else:
			m.display.scroll(result, wait=False, loop=True)
		music.play(music.JUMP_UP)	

update_display()
while True:
	if m.button_b.was_pressed():
		if dice + 1 < len(dices):
			dice += 1
		else:
			dice = 0
		result = None
		update_display()
	elif m.button_a.was_pressed():
		if dice > 0:
			dice -= 1
		else:
			dice = len(dices) - 1
		result = None		
		update_display()
	elif m.accelerometer.was_gesture('shake'):
		result = random.randint(1, dices[dice])
		update_display()
	m.sleep(1)

