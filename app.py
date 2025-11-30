from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from os import environ as ENV

app = Flask(__name__)

@app.get('/')
def visit_page():
    return render_template('index.html')

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, host='0.0.0.0', port=5000)