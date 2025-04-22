# TODO: make a little flaks service that is somehow offering os-command
# injection

from flask import Flask, request, render_template_string
import subprocess
import os

app = Flask("amazing-time-calculator")

@app.route("/", methods=["GET", "POST"])
def index():
    return "YOU FOOL"

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=80)
