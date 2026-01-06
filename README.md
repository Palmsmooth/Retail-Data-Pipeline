# Data Engineering Project: Retail Data Pipeline

This project is from the [Road to Data Engineer](https://pages.datath.com/r2de3-course) course.  
Road to Data Engineer provides fundamental to advanced knowledge in the Data Engineer track, which can be applied to build automated data pipelines.

---

## Project Overview

<img src="image\process-overview.png" width="100%" height="40%">

---

## Stages and Technologies

### 1. Data Collection
Collecting data from various sources (databases and REST APIs) in Google Colab using Python:

- **Step 1:** Reading data from a MySQL database  
- **Step 2:** Fetching currency exchange data from an API using Requests  
- **Step 3:** Joining the data  
- **Step 4:** Output result files  

---

### 2. Data Cleansing
Using Apache Spark (Colab and PySpark):

- **Step 1:** Installation of Spark and PySpark  
- **Step 2:** Data Profiling  
- **Step 3:** EDA (Exploratory Data Analysis)  
- **Step 4:** Data Cleansing with PySpark  
- **Step 5:** Data Export in PySpark  

---

### 3. Data Storage
Using Google Cloud Storage (GCS):

- **Step 1: Creating a Bucket**
  - Method 1: Using the Cloud Console via the web UI  
  - Method 2: Using the gsutil command via Cloud Shell  

- **Step 2: Upload data**
  - Method 1: Upload via Cloud Console using the web UI  
  - Method 2: Use the gsutil command via Cloud Shell  
  - Method 3: Use Python code via the Python SDK library  

---

### 4. Automated Data Pipeline
Using Apache Airflow in Google Cloud Composer:

- **Step 1:** Build a Cloud Composer environment  
- **Step 2:** Manage the Composer environment  
- **Step 3:** Create a MySQL connection  
- **Step 4:** Create an Airflow DAG
  - Importing Modules  
  - Default Arguments  
  - Instantiate the DAG  
  - Tasks  
  - Setting up Dependencies  

---

### 5. Data Warehouse
Using BigQuery (integrated with Airflow):

- **Step 1:**  Create dataset
- **Step 2:** Import data
  - Method 1: Import using the Cloud Console (web-based UI)  
  - Method 2: Import using the bq command via Airflow BashOperator  
  - Method 3: Import using GCSToBigQueryOperator in Airflow  

- **Step 3:** Explore data on BigQuery using SQL  

---

### 6. Dashboard

- **Step 1:** Create a view to provide a specific subset of data for visualization  
- **Step 2:** Create a dashboard