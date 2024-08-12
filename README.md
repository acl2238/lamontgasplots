Short script to display gas data on NYAAQ

Saving here as backup

Quick Instructions (on solas):
tbd

For startup:
1. Use ps -ef to find running processes and kill gasplot if running (usually not needed)
2. Go to screen with 'screen -r' or if there is no screen make one with screen -S namehere
3. source env/bin/activate
4. pip install -r requirements.txt
5. python gasplot.py (That's it!)

It is recommended to run in screen because this process will occupy the existing terminal, you want to run it in background continuous
