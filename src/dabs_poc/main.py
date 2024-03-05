from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, TimestampType, FloatType


def get_taxis():
  spark = SparkSession.builder.getOrCreate()

  schema = StructType([
      StructField("trip_id", StringType(), True),
      StructField("pickup_datetime", TimestampType(), True),
      StructField("dropoff_datetime", TimestampType(), True),
      StructField("passenger_count", IntegerType(), True),
      StructField("trip_distance", FloatType(), True),
      StructField("pickup_location", StringType(), True),
      StructField("dropoff_location", StringType(), True)
  ])

  data = [
    ("1001", "2023-01-01 10:00:00", "2023-01-01 10:30:00", 1, 5.2, "Location A", "Location B"),
    ("1002", "2023-01-01 11:00:00", "2023-01-01 11:15:00", 2, 3.0, "Location C", "Location D"),
    ("1003", "2023-01-01 12:00:00", "2023-01-01 12:45:00", 1, 7.5, "Location E", "Location F"),
    ("1004", "2023-01-02 09:00:00", "2023-01-02 09:30:00", 3, 6.2, "Location G", "Location H"),
    ("1005", "2023-01-02 10:00:00", "2023-01-02 10:20:00", 2, 4.8, "Location I", "Location J"),
    ("1006", "2023-01-02 11:00:00", "2023-01-02 11:10:00", 1, 2.2, "Location K", "Location L"),
    ("1007", "2023-01-02 13:00:00", "2023-01-02 13:30:00", 4, 5.0, "Location M", "Location N"),
    ("1008", "2023-01-03 08:00:00", "2023-01-03 08:15:00", 1, 3.3, "Location O", "Location P"),
    ("1009", "2023-01-03 09:00:00", "2023-01-03 09:45:00", 2, 8.1, "Location Q", "Location R"),
    ("1010", "2023-01-03 10:30:00", "2023-01-03 11:00:00", 3, 6.4, "Location S", "Location T")
  ]

  df = spark.createDataFrame(data, schema=schema)

  return df

  
  #return spark.read.table("samples.nyctaxi.trips")


def main():
  get_taxis().show(5)

if __name__ == '__main__':
  main()
