def key_input(event):
	init()
	print 'Control:', event.char
	key_press = event.char
	sleep_time = 0.030

	if key_press.lower() == 'a':
		#whatever + 1
	elif key_press.lower() == 'd':
		#whatever -1
	else:gpio.cleanup()

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()		