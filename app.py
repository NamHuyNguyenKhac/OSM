from flask import Flask, render_template, request, jsonify
import pandas as pd
import csv

app = Flask(__name__)

def read_csv(file_path):
    markers = []
    with open(file_path, 'r', encoding="utf8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Split the coordinate string into latitude and longitude
            lat, lon = map(float, row['coor'].split())
            markers.append({
                'latitude': lat,
                'longitude': lon,
                'title': row['title'],
                'area': row['area'],
                'bedroom': row['bedroom'],
                'bathroom': row['bathroom'],
                'price': row['price'],
                'description': row['description']
            })
    return markers

@app.route('/')
def home():
    markers = read_csv('data_bds_total.csv')  # Adjust the file path as needed
    return render_template('index.html', markers=markers)

if __name__ == '__main__':
    app.run(debug=True)
