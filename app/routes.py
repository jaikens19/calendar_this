from flask import Blueprint, render_template
import os
import pyscopg2


bp = Blueprint('main', __name__, url_prefix='/')

CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}

@bp.route('/')
def main():
    conn = pyscopg2.connect(**CONNECTION_PARAMETERS)
    curs = conn.cursor()
    curs.execute('SELECT id, name, start_datetime, end_datetime FROM appointments ORDER BY start_datetime;')
    appointments = curs.fetchall()
    print(appointments)


    return render_template('main.html')
