import sys, time

d = raw_input("Despertar (HH:MM): ")
while time.strftime("%H:%M") != d:
	try:
		print "\b\b\b\btick",
		sys.stdout.flush()
		time.sleep(0.5)
		print "\b\b\b\btack",
		sys.stdout.flush()
		time.sleep(0.5)
	except KeyboardInterrupt:
		break
else:
	print "\n\nTRIM\a\a\a"
	sys.exit(0)
print "\n\nInterrompido!"
