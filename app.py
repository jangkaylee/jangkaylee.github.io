from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', names=names)

def add_name():
    if request.method == 'POST':
        name = request.form['name']
        names.append(name)
        return redirect(url_for('index'))
    return redirect(url_for('index'))  # Redirect GET requests back to the landing page

if __name__ == '__main__':
    app.run(debug=True)