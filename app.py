import tabulate
import time

from flask import Flask


app = Flask(__name__)


monitor = {}


@app.route('/')
def hello():
    return 'HACK-2925 is a go!'


@app.route('/healthcheck')
def get_healthcheck():    
    if not monitor:
        return 'No unit checked in yet.'

    return tabulate.tabulate(
        [(k, '%d seconds ago' % (time.time() - v)) for k, v in monitor.items()],
        headers = ['Unit', 'Checked in (seconds ago)'],
        tablefmt='html',
    )


@app.route('/healthcheck/<string:badge>', methods=['PUT'])
def put_healthcheck(badge):
    monitor[badge] = time.time()
    return 'Healthcheck recvd for %s!\n' % badge


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run(host='81.187.191.139')