from flask import Flask, jsonify, render_template

from database import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs_db = load_jobs_from_db()
  return render_template('home.html', jobs=jobs_db, company_name='Simon')


@app.route("/api/jobs")
def list_jobs():
  jobs_db = load_jobs_from_db()
  return jsonify(jobs_db)


#DONE: Learn to change favicon icon

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
