"""Backend code to deploy website to my funtastic portfolio!"""
from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)

@app.get('/')
def visit_page():
    """Return my portfolio page html so ppl can see it"""
    return render_template('index.html')

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, host='0.0.0.0', port=2137)
