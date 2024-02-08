from flask import Flask, render_template, request

app = Flask(__name__)

entries = []

@app.route('/')
def index():
    return render_template('index.html', entries=entries)

@app.route('/submit', methods=['POST'])
def submit():
    entry = request.form['entry']
    entries.append(entry)
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)