# Python app

This Flask application displays the current time in Moscow. 

# Installing

To run this app Python libraries Flask, pytz must be installed:
```bash
> pip install Flask
> pip install pytz
```
# Running

Unix Bash:
```bash
> export FLASK_APP=main.py
> flask run
```
Windows CMD:
```bash
> set FLASK_APP=main.py 
> flask run
```
Windows PowerShell:
```bash
> $env:FLASK_APP = "main.py"
> $flask run
```

## Docker
Docker image was built and committed with:
```bash
> docker build --tag nkt929/devops:latest .
> docker push nkt929/devops:latest         
```

To run it use:
```bash
> docker run -p 5000:5000 nkt929/devops:latest
```   
