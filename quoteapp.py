from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "The best way to predict the future is to invent it. – Alan Kay",
    "Success is not final; failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Simplicity is the soul of efficiency. – Austin Freeman",
    "It always seems impossible until it’s done. – Nelson Mandela"
]

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
