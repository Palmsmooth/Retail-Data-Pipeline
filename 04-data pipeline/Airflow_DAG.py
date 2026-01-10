from airflow.models import DAG
from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.utils.dates import days_ago
import pandas as pd
import requests

MYSQL_CONNECTION = "mysql_default"   #The name of the connection configured in Airflow
CONVERSION_RATE_URL = "https://r2de3-currency-api-vmftiryt6q-as.a.run.app/gbp_thb"

# The output_path variable to be saved
mysql_output_path = "/home/airflow/gcs/data/transaction_data_merged.parquet"
conversion_rate_output_path = "/home/airflow/gcs/data/conversion_rate.parquet"
final_output_path = "/home/airflow/gcs/data/workshop4_output.parquet"

default_args = {
    'owner': 'datath',
}


@dag(default_args=default_args, schedule_interval="@once", start_date=days_ago(1), tags=["workshop"])
def workshop4_pipeline():
    """
    # Exercise 4: Final DAG
    In this exercise, we will take the code previously written in Workshop 1 and turn it into a pipeline on Airflow.
    """
    @task()
    def get_data_from_mysql(output_path):
        # Receive output_path from the task being called

        # Use MySqlHook to connect to MySQL using the connection configured in Airflow
        mysqlserver = MySqlHook(MYSQL_CONNECTION)
        
        # Query the database using the created hook and return the result as a pandas DataFrame
        product = mysqlserver.get_pandas_df(sql="SELECT * FROM r2de3.product")
        customer = mysqlserver.get_pandas_df(sql="SELECT * FROM r2de3.customer")
        transaction = mysqlserver.get_pandas_df(sql="SELECT * FROM r2de3.transaction")

        # Merge data from two DataFrames as in Workshop 1
        merged_transaction = transaction.merge(product, how="left", left_on="ProductNo", right_on="ProductNo").merge(customer, how="left", left_on="CustomerNo", right_on="CustomerNo")
        
        # Save the Parquet file to the provided output_path
        # It will be stored in GCS automatically
        merged_transaction.to_parquet(output_path, index=False)
        print(f"Output to {output_path}")

    @task()
    def get_conversion_rate(output_path):
        # Send a request to retrieve data from CONVERSION_RATE_URL
        r = requests.get(CONVERSION_RATE_URL)
        result_conversion_rate = r.json()
        df = pd.DataFrame(result_conversion_rate)
        df = df.drop(columns=['id'])

        # Convert the column to a date type and save the file as Parquet
        df['date'] = pd.to_datetime(df['date'])
        df.to_parquet(output_path, index=False)
        print(f"Output to {output_path}")

    @task()
    def merge_data(transaction_path, conversion_rate_path, output_path):

        # Read from the file, noting that the path is taken from the provided parameter
        transaction = pd.read_parquet(transaction_path)
        conversion_rate = pd.read_parquet(conversion_rate_path)

        # merge 2 DataFrame
        final_df = transaction.merge(conversion_rate, how="left", left_on="Date", right_on="date")
        
        # Convert the price into total_amount and thb_amount
        final_df["total_amount"] = final_df["Price"] * final_df["Quantity"]
        final_df["thb_amount"] = final_df["total_amount"] * final_df["gbp_thb"]

        # Drop unused columns and rename the columns
        final_df = final_df.drop(["date", "gbp_thb"], axis=1)

        final_df.columns = ['transaction_id', 'date', 'product_id', 'price', 'quantity', 'customer_id',
            'product_name', 'customer_country', 'customer_name', 'total_amount','thb_amount']

        # save Parquet file
        final_df.to_parquet(output_path, index=False)
        print(f"Output to {output_path}")
        print("== End of Workshop 4 ʕ•́ᴥ•̀ʔっ♡ ==")

    
    t1 = get_data_from_mysql(output_path=mysql_output_path)

    t2 = get_conversion_rate(output_path=conversion_rate_output_path)

    t3 = merge_data(
            transaction_path=mysql_output_path,
            conversion_rate_path=conversion_rate_output_path,
            output_path=final_output_path
        )

    [t1, t2] >> t3

workshop4_pipeline()