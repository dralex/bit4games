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

def update_display():
	m.display.scroll('d' + str(dices[dice]), wait=False, loop=True)
	music.play(music.POWER_UP)

update_display()
while True:
	if m.button_b.was_pressed():
		if dice + 1 < len(dices):
			dice += 1
		else:
			dice = 0
		update_display()
	elif m.button_a.was_pressed():
		if dice > 0:
			dice -= 1
		else:
			dice = len(dices) - 1
		update_display()
	elif m.accelerometer.was_gesture('shake'):
		r = random.randint(1, dices[dice])
		if r < 10:
			m.display.show(r)
		else:
			m.display.scroll(r, wait=False, loop=True)
		music.play(music.JUMP_UP)
	m.sleep(10)

