from databricks.connect import DatabricksSession
from pyspark.sql import SparkSession
from dabs_poc import main
import great_expectations as ge

# Create a new Databricks Connect session. If this fails,
# check that you have configured Databricks Connect correctly.
# See https://docs.databricks.com/dev-tools/databricks-connect.html.

SparkSession.builder = DatabricksSession.builder
SparkSession.builder.getOrCreate()

def test_main():
    taxis = main.get_taxis()
    assert taxis.count() > 5


def test_tpep_pickup_datetime_not_null():
    taxis = main.get_taxis()
    gedf = ge.dataset.SparkDFDataset(df)

    # Load the expectation suite (adjust the path and suite name as necessary)
    suite = gedf.get_expectation_suite('your_expectation_suite_name.json')

    # Validate the DataFrame against the expectation suite
    results = gedf.validate(expectation_suite=suite)

    # Ensure the test fails if Great Expectations finds any validation failures
    assert results['success'] is True, "Data quality check failed for tpep_pickup_datetime column."
