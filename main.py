# Run this script, NOT gasplot.py!

import subprocess
import time

while True:
	subprocess.run("timeout 24h gunicorn gasplot:server -b :8050".split(' '))
	subprocess.run("pkill gunicorn".split(' '))
	print("hello!!!")
	time.sleep(5)
