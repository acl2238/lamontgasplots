Short script to display gas data on NYAAQ

Saving here as backup

Quick Instructions (on solas):
tbd

For startup:
1. Use ps -ef to find running processes and kill gasplot if running
2. Go to screen with 'screen -r' or if there is no screen make one with screen -S namehere
3. source env/bin/activate
4. gunicorn gasplot:server -b :8050 (or whatever port number you want really, but probably use this one lolz)


