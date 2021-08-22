import datetime

from flask import Flask
import pytz


app = Flask(__name__)


@app.route("/", methods=['GET'])
def get_time():
    tz_moscow = pytz.timezone('Europe/Moscow')
    datetime_moscow = datetime.datetime.now(tz_moscow)
    server_time = datetime_moscow.strftime('%A %B, %d %Y %H:%M:%S')
    return "server time {}".format(server_time)
