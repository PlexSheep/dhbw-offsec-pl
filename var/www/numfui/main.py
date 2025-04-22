from flask import Flask, request, render_template, logging
from logging import getLogger
from wtforms import Form, IntegerField, StringField, validators
import subprocess
import os

app = Flask("numfui")

class FormatForm(Form):
    number = StringField("number", [validators.Length(max=80)])
    format = StringField("format", [validators.Length(min=3, max=3)])

FMT_TO_FLAG = {
    "bin": "-b",
    "hex": "-x",
    "oct": "-o",
    "b64": "-s",
    "b32": "-z",
    "dec": "-d",
}

def get_format_flag(fmt: str | None) -> str:
    val = FMT_TO_FLAG[fmt.strip()]
    if val is None: 
        raise Exception("Unknown format")
    return val

@app.route("/", methods=["GET", "POST"])
def index():
    form = FormatForm(request.form)
    output: str = ""
    if request.method == "POST":
        logger = app.logger
        if not form.validate():
            logger.warning(f"The form was bad: {form.data}")
        try:
            cmd = f"/home/dave/.local/bin/numf {form.number.data} {get_format_flag(form.format.data)}"
            logger.info(f"cmd: {cmd}")
            output: str = subprocess.check_output(cmd, shell=True).decode()
            logger.info(f"output: {output}")
        except subprocess.CalledProcessError as e:
            logger.warning(f"The subprocess failed: {e}")
            logger.warning(f"STDOUt of fail: {e.stdout.decode()}")
        except Exception as e:
            logger.warning(f"Could not format: {e}")
            output = "Error :("
    return render_template("index.html", output=output)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
