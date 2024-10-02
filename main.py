from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL
conn = psycopg2.connect(dbname="osm_db", user="postgres", password="665667", host="localhost")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_parks')
def get_parks():
    cur = conn.cursor()
    cur.execute("SELECT ST_AsGeoJSON(way) FROM planet_osm_polygon WHERE leisure='park';")
    parks = cur.fetchall()
    cur.close()
    return jsonify(parks)

if __name__ == '__main__':
    app.run(debug=True)
