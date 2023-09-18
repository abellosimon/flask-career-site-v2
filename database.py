from sqlalchemy import create_engine, text
import os

engine = create_engine(
    os.environ['DB_CONNECTION_STRING'],
    connect_args={"ssl": {
        "ca": "/etc/ssl/certs/ca-certificates.crt"
    }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs
