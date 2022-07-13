from flask import Flask
from flask.wrappers import Response
from requests import get

app = Flask(__name__)

@app.get('/')
def index() -> str:
    return '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Fetch A License</title>
    </head>
    <body>
        <h1>Fetch A License</h1>
        <p>
            Retrieve the plaintext representation of a software license by its
            <a target="_blank" href="https://spdx.org/licenses/">SPDX</a>
            identifier.
        </p>

        <h2>Example Usages:</h2>
        <p><code>$ curl https://fetchalicense.com/Apache-2.0 > LICENSE</code></p>
        <p><code>$ curl https://fetchalicense.com/CC0-1.0 > LICENSE</code></p>
        <p><code>$ curl https://fetchalicense.com/GPL-3.0-or-later > COPYING</code></p>
        <p><code>$ curl https://fetchalicense.com/MIT > LICENSE</code></p>
        <p><code>$ curl https://fetchalicense.com/Unlicense > LICENSE</code></p>
        
        <p><a target="_blank" href="https://github.com/jsvcycling/fetchalicense">Source Code</a></p>
    </body>
</html>
    '''

@app.get('/<spdx>')
def get_license(spdx: str) -> Response:
    license_text = get(f'https://raw.githubusercontent.com/spdx/license-list-data/master/text/{spdx}.txt')
    res = Response(str(license_text.text), 200)
    res.headers['Content-Type'] = 'text/plain'
    return res
