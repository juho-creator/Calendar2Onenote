
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# prints "hello world" without page refreshed  
@app.route('/button_pressed', methods=['POST'])
def button_pressed():
    print("Hello, world!")
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
