import csv
from flask import Flask,render_template,request
app = Flask(__name__)

app.config['SECRET_KEY'] = '202977e7b6cb385ae79442a0492fb179'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/collection')
def collection():
    return render_template("collection.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/entertainment')
def entertainment():
    return render_template("entertainment.html")

@app.route('/locations')
def locations():
    return render_template("locations.html")

@app.route('/environment')
def environment():
    return render_template("environment.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/conferences')
def conferences():
    return render_template("conferences.html")

@app.route('/conferences', methods=['POST'])
def handle_request():
    with open('data/messages.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([request.form['name'],
                         request.form['email'],
                         request.form['date']])
    return render_template('response.html', data=request.form)


if __name__ == '__main__':
    app.run(debug = True)
