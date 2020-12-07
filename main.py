#!/usr/bin/env python

import yaml

from flask import Flask
from flask.templating import render_template
from time import time
from hashlib import md5

app = Flask(__name__)

app.static_folder = './static/'
app.template_folder = './templates/'

def parse_yaml(filename='./static/my_resume.yaml'):
    with open(filename) as file:
        cv = yaml.full_load(file)
        cv['cachebuster'] = lambda: md5(str(time())).hexdigest()
    return cv


@app.route('/')
def main():
    return render_template("main.html", content=parse_yaml())


if __name__ == '__main__':
    app.run()
