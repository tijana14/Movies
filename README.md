# Movies

# Data Pipeline Project

This project demonstrates a simple data pipeline that processes and analyzes raw data from a CSV file.


## 🧱 Pipeline Overview

The pipeline includes the following steps:

1. **Data Ingestion** – Loading the raw data from a CSV file.
2. **Data Cleaning** – Handling missing values, duplicates, and inconsistent formatting.
3. **Data Transformation** – Creating new features, filtering data, and formatting columns.

## 📂 Project Structure

project/
│
├── data/
│ └── movies.csv # Raw input data
│
├── pipeline/
│ ├── load_data.py # Data loading logic
│ ├── clean_data.py # Cleaning functions
│ ├── transform_data.py # Transformation steps
│ └── analyze.py # Analysis and visualization
│
├── main.py # Entry point to run the pipeline
├── requirements.txt # Python dependencies
└── README.md # Project instructions

## 🚀 How to Run

1. Clone the repository:

git clone https://github.com/your-username/data-pipeline.git
cd data-pipeline
(Optional) Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required packages:

pip install -r requirements.txt
Run the pipeline:

python main.py

📊 Output
Cleaned dataset saved in /output/clean_data.csv

Summary statistics printed to the console

You can modify the pipeline or individual scripts depending on your use case.

👤 Author
Tijana Dajić
