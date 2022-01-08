import os

from flask import Flask, render_template, send_from_directory, Response
from npoapi import Media
import json

app = Flask(__name__)

client = Media(interactive=False,
               debug=os.getenv("debug", default=False)
               ).configured_login(config_dir=os.getenv("configdir"), default_config_dirs=False)
client.env("prod")

@app.route('/')
@app.route('/<path:mid>')
def index(mid = None):
    # Opening JSON file
    with open(os.fspath('examples.json')) as json_file:
        examples = json.load(json_file)
    return render_template('index.html', mid=mid, examples=examples)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/mediaobject/<path:mid>')
def send_mediaobject(mid):
    all_properties = ["all"]
    properties =  ["title:main:1",
           "locations",
           "predictionsForXml", # NPA-602
           "predictions"]
    proxied_response = client.get(mid, accept="application/json", stream=False, properties=all_properties)

    response = Response(proxied_response, mimetype='application/json')
    return response


@app.route('/authenticate/<path:uri>')
def authenticate(uri):
    return client.authenticate(uri, interactive=False)

if __name__ == "__main__":
    app.run(debug=True)
