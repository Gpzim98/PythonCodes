import sys
import time

despertar = raw_input("Despertar (HH:MM): ")

while time.strftime("%H:%M") != despertar:
    try:
        print "\b\b\b\b\btick",
        sys.stdout.flush()
        time.sleep(1)
        print "\b\b\b\b\btack",
        sys.stdout.flush()
        time.sleep(1)
    except KeyboardInterrupt:
        break
else:
    print "\n\nTRIM!\a\a\a"
    sys.exit(0)

print "\n\nInterrompido!"
