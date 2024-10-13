from flask import Flask, render_template
import psycopg2
import pandas as pd

app = Flask(__name__)

# Connect to PostgreSQL
conn = psycopg2.connect(dbname="osm_db", user="postgres", password="665667", host="localhost")

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
