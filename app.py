from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Flask"

@app.route('/data')
def get_data():
    for i in range(1, 1001):
        yield f"data: hello from Python {i}\n\n"
        time.sleep(0.5)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
