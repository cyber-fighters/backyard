"""A webapp."""
import os

import flask


app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def request_result():
    """Call TheHarvester."""
    # define output files
    _result_file = "/data/scan_results/{}/data_theharvester.html".format(flask.request.form['id'])

    # define command
    _data_source = "bing"
    _cmd = "theharvester -d {} -b {} -f {}".format(flask.request.form['domain'], _data_source, _result_file)

    # run it
    print("Executing: " + _cmd)
    os.system(_cmd)

    # return something
    return 'Finished: ' + _cmd


if __name__ == '__main__':
    _port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=_port)
