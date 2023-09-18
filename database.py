import os

from sqlalchemy import create_engine, text

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


def load_job_from_db(id):
  try:
    with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),
                            {'val': id})
      row = result.fetchone()
      if row is None:
        return None
      else:
        return row._asdict()
  except Exception as e:
    print(f"Error fetching job with ID {id}: {e}")
    return None
