import flask
from flask import Flask, request, render_template
import os
import json
import main

app = Flask(__name__, static_folder='../../static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_end_predictions', methods=['post'])
def get_prediction_eos():
    try:
        in_txt = ' '.join(request.json['input_text'].split())
        in_txt += ' <mask>'
        top_k = request.json['top_k']
        res = main.get_all_predictions(in_txt, top_clean=int(top_k))
        return app.response_class(response=json.dumps(res), status=200, mimetype='application/json')
    except Exception as error:
        err = str(error)
        print(err)
        return app.response_class(response=json.dumps(err), status=500, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 8080)))
