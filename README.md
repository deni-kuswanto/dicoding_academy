# Streamlit Dashboard to Analyze "Bike Sharing" Data

## Description
This dashboard was created using Streamlit to analyze bike sharing data. It displays various data analysis and visualizations such as total bookings, best and worst products, customer demographics, and RFM analysis.

## Prerequisite
Before running this application, make sure you have installed Python and the numpy, pandas, matplotlib, seaborn, scikit-learn, and streamlit libraries. You will also need a CSV data file containing bike sharing information.

### Python Installation
If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

### Library Installation
1. Clone this repository or download it as a ZIP.
2. Navigate to the project directory.
3. Create a `requirements.txt` file using the following list of libraries:

```
matplotlib 3.9.2
numpy 2.1.2
pandas 2.2.3
scikit-learn 1.5.2
seaborn 0.13.2
streamlit 1.39.0

```

4. Install all dependencies using the following command:

pip install (library you want to install)

## Providing Data
Make sure you have a data file named `all_data.csv` in your project directory. This file should have the appropriate columns for analysis, including:

- `Peak Usage Time`
- `Total Rides`
- `Weather Condition`
- `Hour`

## Running the Application
Once all dependencies are installed and data files are provided, you can run the Streamlit dashboard with the following steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the `dashboard.py` file is located.
3. Run the following command:
    
    streamlit run dashboard.py
    

4. Once the command is executed, the application will open in your browser at the address `http://localhost:8501`.

## Features
- **Daily Analysis**: Shows total orders and revenue per day.
- **Best and Worst Products**: Shows the most and least sold products.
- **Customer Demographics**: Shows the number of customers by gender and age group.
- **RFM Analysis**: Presents analysis based on Recency, Frequency, and Monetary of customers.

## Conclusion
This dashboard is a useful tool for analyzing bike sharing data and gaining deeper insights into service usage.



Hasil streamlit bisa di lihat di

https://dicodingacademy-yvcihklqt9odxyfvam4qrd.streamlit.app/

repository github untuk proyek ini

https://github.com/deni-kuswanto/dicoding_academy

