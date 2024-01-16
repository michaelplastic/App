from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Function to generate a random color
def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Generate a new random color when the form is submitted
        background_color = generate_random_color()
    else:
        # Generate a random color for the initial page load
        background_color = generate_random_color()
    return render_template('index.html', background_color=background_color)

@app.route('/bat-attack')
def bat_attack():
    return render_template('bat_attack.html')

if __name__ == '__main__':
    # Use 0.0.0.0 to make the app accessible from outside the container
    app.run(host='0.0.0.0', port=8000, debug=True)

