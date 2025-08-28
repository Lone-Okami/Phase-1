import pandas as pd

weather_data = [] # List to hold and structure data

# Load data using pandas module
def load_csv_pandas(file_name):
    df = pd.read_csv(file_name)
    return df

# appends content to the list "weather_data"
def add_to_weather_data(content):
    for lines in content:
        weather_data.append(lines)

# execution
if __name__ == '__main__':
    file_name = "AustraliaWeatherData/Weather Training Data.csv"
    df = load_csv_pandas(file_name)
    print("Number of entries:", len(df))
    print("Description of the data:")
    print(df.describe())

