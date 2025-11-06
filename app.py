from flask import Flask, render_template, request, send_from_directory
import os
import pandas as pd
from summarizer import summarize_bid
from scorer import score_bid
from report_generator import generate_pdf

UPLOAD_FOLDER = "bids"
REPORT_FOLDER = "reports"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Process CSV
    bids = pd.read_csv(filepath)
    bids['summary'] = bids['bid_text'].apply(summarize_bid)
    bids['score'] = bids.apply(score_bid, axis=1)
    top_bids = bids.sort_values(by='score', ascending=False).head(10)

    # Generate report
    report_filename = f"{os.path.splitext(file.filename)[0]}_report.pdf"
    report_path = os.path.join(REPORT_FOLDER, report_filename)
    generate_pdf(top_bids, report_path)

    return render_template("index.html", report=report_path)

@app.route("/reports/<path:filename>")
def download_report(filename):
    return send_from_directory(REPORT_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
