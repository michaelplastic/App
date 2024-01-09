from flask import Flask, render_template
import random

app = Flask(__name__)

# List of cute colors
cute_colors = ['#FFB6C1', '#FF69B4', '#FF1493', '#FFC0CB', '#FFD700', '#FF4500']

@app.route('/')
def index():
    # Choose a random cute color
    chosen_color = random.choice(cute_colors)
    return render_template('index.html', color=chosen_color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

