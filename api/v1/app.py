import sys
import os
from flask import Flask, request, jsonify
import pandas as pd

from diversity_metrics.classification.Pairwise.pairwise_metrics import CorrelationCoefficient ,QStatistics # Import your metric module


app = Flask(__name__)

# Endpoint to upload and load Excel file
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if not file.filename.endswith(('.xls', '.xlsx')):
        return jsonify({"error": "Invalid file type. Please upload an Excel file."}), 400

    file_path = os.path.join('/tmp', file.filename)
    file.save(file_path)

    # Load the Excel file into a pandas DataFrame
    try:
        df = pd.read_excel(file_path)
        columns = df.columns.tolist()
        return jsonify({"columns": columns, "file_path": file_path}), 200  # Send back available columns and file path
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to calculate a selected metric
@app.route('/calculate', methods=['POST'])
def calculate_metrics():
    data = request.json
    file_path = data.get('file_path')  # Assume the file path is passed
    selected_columns = data.get('columns')

    print("Selected columns: ", selected_columns)
    metric_name = data.get('metric', '')


    if not selected_columns or len(selected_columns) < 2:
        return jsonify({"error": "Please select at least two columns."}), 400

    try:
        # Load the file and select columns
        df = pd.read_excel(file_path)

        
        y1, y2 = df[selected_columns[0]], df[selected_columns[1]]
        y_true = df[selected_columns[2]] if len(selected_columns) > 2 else None

    

        # Dynamically choose the metric to calculate
        if metric_name == 'correlation_coefficient':
            correlation_metric = QStatistics(y_1=y1, y_2=y2, y_true=y_true)
            result = correlation_metric.calculate()
            print("Result: ", result)
        else:
            return jsonify({"error": f"Metric {metric_name} is not supported."}), 400

        return jsonify({"metric": metric_name, "result": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=5000)
