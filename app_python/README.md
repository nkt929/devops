# Python app

This Flask application displays the current time in Moscow. 

#Installing

To run this app Python libraries Flask, pytz must be installed:
```bash
> pip install Flask
> pip install pytz
```
#Running

Unix Bash:
```bash
> export FLASK_APP=app.py\
> flask run
```
Windows CMD:
```bash
> set FLASK_APP=app.py 
> flask run
```
Windows PowerShell:
```bash
> $env:FLASK_APP = "app.py"
> $flask run
> ```