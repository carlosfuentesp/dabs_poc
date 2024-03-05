from databricks.connect import DatabricksSession
from pyspark.sql import SparkSession
from dabs_poc import main
import great_expectations as ge


SparkSession.builder = DatabricksSession.builder
SparkSession.builder.getOrCreate()

def test_main():
    taxis = main.get_taxis()
    assert taxis.count() > 5


def test_tpep_pickup_datetime_not_null():
    taxis = main.get_taxis()
    gedf = ge.dataset.SparkDFDataset(taxis)
    column_name = "passenger_count"

    assert gedf.expect_column_values_to_not_be_null(column_name)['success'] == True, \
            f"Column '{column_name}' contains null values"
