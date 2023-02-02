from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'verysecretkey'
toolbar = DebugToolbarExtension(app)

@app.route('/')
def main():
    return render_template('test.html')


@app.route('/departures/<departure>/')
def dep(departure):
    return render_template('departure.html', departure=departure)


@app.route('/tours/<id>/')
def render_products(id):
    return render_template('tour.html', id=id)


if __name__ == "__main__":
    app.run()
