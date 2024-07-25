from flask import Flask, render_template, jsonify, request
import pandas as pd

app = Flask(__name__)

# Path to the CSV file
CSV_FILE_PATH = "/home/kali/Desktop/all_server_health.csv"

# Function to read CSV data
def read_csv_data():
    df = pd.read_csv(CSV_FILE_PATH)
    data = df.to_dict(orient='records')
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def data():
    location = request.args.get('location', 'All')
    data = read_csv_data()
    if location != 'All':
        data = [row for row in data if row['Location'] == location]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='127.0.01' , port=5000, ssl_context=('certificate.crt', 'private.key'))

