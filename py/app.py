import time
from datetime import datetime
from flask import Flask

TIMEOUT = 5
app = Flask(__name__)

@app.route("/")
def ping():
  return "python - ping"

@app.route("/timeout")
def timeout():
  time.sleep(TIMEOUT)
  return "python - timeout"

@app.route("/heavy")
def heavy():
	start = datetime.now()
	while True:
		now = datetime.now()
		if (now - start).seconds >= TIMEOUT:
			break
	return "python - heavy"