from flask import Flask, request, jsonify, render_template
import torch
from model.model import ChatModel
from utils.nlp import preprocess
from utils.responses import get_response, safety_check

app = Flask(__name__)

# minimal model placeholder
model = ChatModel()
model.eval()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json or {}
    text = data.get('message', '')
    flagged = safety_check(text)
    if flagged.get('urgent'):
        return jsonify({'reply': flagged['message'], 'meta': {'flag': 'urgent'}})
    tokens = preprocess(text)
    reply = get_response(model, tokens)
    return jsonify({'reply': reply, 'meta': {}})

if __name__ == '__main__':
    app.run(debug=True)
