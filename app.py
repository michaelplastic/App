from flask import Flask, render_template
import random

app = Flask(__name__)

# List of colors
colors = ['#FFB6C1', '#FF69B4', '#FF1493', '#FFC0CB', '#FFD700', '#FF4500']

@app.route('/')
def menu():
    return render_template('main.html')

@app.route('/color-web-app')
def index():
    # Choose a random color
    chosen_color = random.choice(colors)
    return render_template('index.html', color=chosen_color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

