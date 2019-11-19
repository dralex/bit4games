# -----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# bit4games collection
#
# Level counter program
#
# Author: Alexey Fedoseev <aleksey@fedoseev.net>, 2019
# -----------------------------------------------------------------------------

import microbit as m

level = 1
m.display.clear()

while True:
	if m.button_a.was_pressed() and level > 1:
		level -= 1
	elif m.button_b.was_pressed() and level < 20:
		level += 1
	m.display.show(level)
	m.sleep(100)

