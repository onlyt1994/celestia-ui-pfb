from flask import Flask, render_template, request, redirect, url_for, jsonify
from envi import DEFAULT_NODE_URL, DEFAULT_GAS_LIMIT, DEFAULT_FEE
import logging

app = Flask(__name__)

logger = logging.basicConfig(
    filename='celestia_payforblob.log',
    level=logging.DEBUG
)



@app.route('/')
def index():
    """ Home page
    """
    return render_template('index.html', gas_limit=DEFAULT_GAS_LIMIT, fee=DEFAULT_FEE, node_url=DEFAULT_NODE_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
