from flask import Flask, render_template, request, jsonify
import psycopg2
import pandas as pd
import csv

app = Flask(__name__)

# Store markers in memory (reset when the server restarts)
markers = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_markers', methods=['GET'])
def get_markers():
    data_list = []
    with open('data_bds_total.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_list.append(row)
    return jsonify(data_list)

@app.route('/data')
def data():
    # Read the CSV file and store the data
    data_list = []
    with open('data_bds_total.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_list.append(row)
    return render_template('data.html', data=data_list)

if __name__ == '__main__':
    app.run(debug=True)
