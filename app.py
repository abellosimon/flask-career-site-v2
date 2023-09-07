from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Rotterdam, Netherlands',
    'salary': 'EUR 80,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Amsterdam, Netherlands',
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'EUR 100,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': 'USD 250,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Simon')


@app.route("/api//jobs")
def list_jobs():
  return jsonify(JOBS)


#DONE: Learn to change favicon icon

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
