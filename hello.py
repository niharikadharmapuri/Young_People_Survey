from flask import Flask, request
import pandas as pd
import numpy as np
import json
import pickle
import os


app=Flask(__name__)
@app.route('/api', methods=['POST'])
def make_prediction():
    data=request.get_json(force=True)
    name=data['name']
    return f'hello{name}'

if __name__ == '__main__':
    app.run(port=10001, debug=True)