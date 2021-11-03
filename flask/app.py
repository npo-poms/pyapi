import os

from flask import Flask, render_template, send_from_directory, Response
from npoapi import Media

app = Flask(__name__)

client = Media(interactive=False,
               debug=os.getenv("debug", default=False)
               ).configured_login(config_dir=os.getenv("configdir"), default_config_dirs=False)
client.env("prod")

@app.route('/')
@app.route('/<path:mid>')
def index(mid = None):
    return render_template('index.html', mid=mid)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/mediaobject/<path:mid>')
def send_mediaobject(mid):
    json = client.get(mid, accept="application/json")
    return Response(json, mimetype='application/json')


