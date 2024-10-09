from flask import Flask, render_template
import psycopg2
import pandas as pd

app = Flask(__name__)

# Connect to PostgreSQL
conn = psycopg2.connect(dbname="osm_db", user="postgres", password="665667", host="localhost")

@app.route('/')
def index():
    def locations():
        # Read the CSV file
        df = pd.read_csv('data_bds_total.csv')
        # Split the 'coor' column into latitude and longitude
        df[['latitude', 'longitude']] = df['coor'].str.split(' ', expand=True)
        df['latitude'] = df['latitude'].astype(float)
        df['longitude'] = df['longitude'].astype(float)
        # Convert the DataFrame to a dictionary
        locations = df[['title', 'latitude', 'longitude']].to_dict(orient='records')
        return jsonify(locations)
    return render_template('index.html')

@app.route('/home')
def locations():
    # Read the CSV file
    df = pd.read_csv('data_bds_total.csv')
    # Split the 'coor' column into latitude and longitude
    df[['latitude', 'longitude']] = df['coor'].str.split(' ', expand=True)
    df['latitude'] = df['latitude'].astype(float)
    df['longitude'] = df['longitude'].astype(float)
    # Convert the DataFrame to a dictionary
    locations = df[['title', 'latitude', 'longitude']].to_dict(orient='records')
    return jsonify(locations)


@app.route('/get_parks')
def get_parks():
    cur = conn.cursor()
    cur.execute("SELECT ST_AsGeoJSON(way) FROM planet_osm_polygon WHERE leisure='park';")
    parks = cur.fetchall()
    cur.close()
    return jsonify(parks)

if __name__ == '__main__':
    app.run(debug=True)
