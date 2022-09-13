# Define functions for converting timestamp to datetime object

from datetime import datetime


def timestamp_to_dt(ts):
    dt_object = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    return dt_object

# Function to convert lat and longi from ddmm.mmmm format to dd.dddd format

def convert_to_decimal_degree(value):
    degree = int(value) // 100
    mins = value - 100*degree
    return degree + (mins/60)