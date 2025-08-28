# Weather Data Analysis Project

This project is a Python script that loads, stores, and performs basic analysis on a weather dataset from a CSV file.

## Installation

This project requires the pandas library. Use the package manager pip to install it.

```bash
pip install pandas
```
You will also need to download a Weather dataset of your choice on a website like kaggle.com
## Usage

```python
import pandas as pd

weather_data = []

def load_csv_pandas(file_name):
    df = pd.read_csv(file_name)
    return df

def add_to_weather_data(content):
    for lines in content:
        weather_data.append(lines)

if __name__ == '__main__':
    file_name = "AustraliaWeatherData/Weather Training Data.csv"
    df = load_csv_pandas(file_name)
    print("Number of entries:", len(df))
    print(df.describe())
```

## Contributing

Contributions Welcome

## License

[MIT](https://choosealicense.com/licenses/mit/)