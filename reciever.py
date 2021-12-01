from flask import Flask, request, abort
from dataSender import filtre

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        filtre(request.json)
        return(print('working'))
    else:
        abort(400)

if __name__ == '__main__':
    app.debug = True
    app.run()