# -----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# bit4games collection
#
# Level counter program
#
# Author: Alexey Fedoseev <aleksey@fedoseev.net>, 2019
# -----------------------------------------------------------------------------

from microbit import *

level = 1
microbit.display.clear()

while True:
	if button_a.is_pressed() and level > 1:
		level -= 1
	elif button_b.is_pressed() and level < 20:
		level += 1
	microbit.display.scroll(level)
	sleep(100)

