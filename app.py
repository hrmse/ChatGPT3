# !/usr/bin/env python3

# import main Flask class and request object
from flask import Flask, request
import openai, os, sys,json
from datetime import datetime
from flask_cors import CORS
import pytz

# create the Flask app
app = Flask(__name__)
CORS(app)
@app.route('/ask', methods=['GET'])
def chatgpt():
    prompt = "where is iran"
    args=request.args
    openai.api_key = "Your-API-Key-Here"
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(args['q']),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    iran_tz = pytz.timezone('Asia/Tehran')
    dt = datetime.now(tz=iran_tz)
    return {
        'isQuestion': False,
        "body": message,
        "date": dt
    }

if __name__ == '__main__':
    # run app in debug mode on port 8000
    app.run(debug=False, port=8000)



