# csis4260-assignment1
Data Engineering

Environment Setup

This project was developed within a virtual environment to ensure consistent dependency management and reproducibility. The environment was created using Conda, and all required packages were installed within the environment. The configuration of the environment was exported and saved in an environment.yml file so that the setup can be easily recreated.
To recreate the environment, the following commands can be used:
conda create -n csis4260a1 python=3.11 -y
conda activate csis4260a1
pip install pandas polars pyarrow fastparquet numpy scikit-learn matplotlib streamlit psutil
conda env export > environment.yml
This setup ensures that all dependencies required for data processing, benchmarking, machine learning, and visualization are installed and consistent across systems.

Dataset
The dataset used in this assignment is located at:
data/allstocks5yr.csv
This dataset contains historical stock market data for multiple companies over a five-year period. The attributes included in the dataset are:
Date
Open price
High price
Low price
Close price
Volume
Company name
As required by the assignment instructions, the repository contains only the original dataset.

Part 1 – CSV vs Parquet
The first part of the assignment evaluates the performance differences between CSV and Parquet file formats.
CSV (Comma-Separated Values) is a widely used text-based format that stores data in a row-oriented structure. While it is simple and highly compatible with many systems, it does not provide efficient compression and may lead to slower read times when handling large datasets.
Parquet, in contrast, is a column-oriented storage format designed for analytical workloads. It supports efficient compression and allows selective column reading, which can significantly improve performance during data processing tasks.
To evaluate the performance of both formats, the dataset was scaled to 1×, 10×, and 100× sizes and used for benchmarking experiments.
The results showed that Parquet files were significantly smaller due to compression and generally loaded faster than CSV files, particularly as the dataset size increased. These results demonstrate that Parquet is more suitable for large-scale analytical workloads and big data processing environments.

Part 2 – Pandas vs Polars
The second part of the assignment compares two Python libraries for data processing: Pandas and Polars.
Pandas is one of the most widely used data analysis libraries in Python. It provides powerful tools for data cleaning, transformation, and analysis, and it integrates well with many machine learning frameworks.
Polars is a newer data processing library designed for high performance and memory efficiency. It utilizes parallel execution and column-based processing, allowing it to handle large datasets more efficiently than traditional libraries.
Benchmarking tests indicated that Polars consistently loaded datasets faster than Pandas, and data transformations were also performed more efficiently.
However, Pandas was ultimately used for the machine learning preparation stage because many machine learning libraries, including scikit-learn, operate directly with Pandas DataFrames.
Feature Engineering
Two additional indicators were added to the dataset to support predictive modeling.
SMA20 (Simple Moving Average) calculates the average closing price over the previous 20 days. This indicator helps identify long-term price trends and smooth out short-term fluctuations.
Price Change represents the difference between the current day’s closing price and the previous day’s closing price. This feature captures short-term price momentum.
These engineered features were used as input variables in the machine learning models.
Machine Learning Models
Two machine learning models were implemented to predict the next day’s closing price.
Linear Regression was used as a baseline model. This algorithm models the relationship between variables using a linear equation and provides a simple benchmark for predictive performance.
Random Forest Regressor is an ensemble learning method based on multiple decision trees. It is capable of capturing more complex relationships in the data and often produces more accurate predictions.
The dataset was divided using an 80/20 train-test split, where 80% of the data was used for training and 20% for testing.
Model performance was evaluated using Mean Absolute Error (MAE), which measures the average absolute difference between predicted and actual values.
Visualization Dashboard
A simple interactive dashboard was developed using Streamlit to visualize the prediction results.
The dashboard enables users to:
Select a specific company ticker
View a graphical comparison between actual stock prices and predicted prices
To run the dashboard locally, use the following command:
streamlit run app/app.py
Screenshots of the dashboard interface are included in the final assignment submission.
Notes
The scaled datasets (10× and 100×) created for benchmarking purposes were not included in the repository in order to comply with the assignment submission requirements.
