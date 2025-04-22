# TODO: make a little flaks service that is somehow offering os-command
# injection

from flask import Flask, request, render_template, logging
from logging import getLogger
from wtforms import Form, IntegerField, StringField, validators
import subprocess
import os

app = Flask("numfui")

class FormatForm(Form):
    number = StringField("number", [validators.Length(max=40)])
    format = StringField("format", [validators.Length(min=3, max=3)])

@app.route("/", methods=["GET", "POST"])
def index():
    form = FormatForm(request.form)
    output: str = ""
    if request.method == "POST":
        logger = app.logger
        if not form.validate():
            logger.warning(f"The form was bad: {form.data}")
        try:
            cmd = f"/home/dave/.local/bin/numf {form.number.data}"
            logger.info(f"cmd: {cmd}")
            output: str = subprocess.check_output(cmd, shell=True).decode()
            logger.info(f"output: {output}")
        except subprocess.CalledProcessError as e:
            logger.warning(f"The subprocess failed: {e}")
            output = f"Error :( {e.stdout.decode()}"
    return render_template("index.html", output=output)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
