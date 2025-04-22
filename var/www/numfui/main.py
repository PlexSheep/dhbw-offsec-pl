# TODO: make a little flaks service that is somehow offering os-command
# injection

from flask import Flask, request, render_template
import subprocess
import os

app = Flask("numfui")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
