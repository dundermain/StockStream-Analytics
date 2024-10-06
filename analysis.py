import os
import json
import pandas as pd
import matplotlib.pyplot as plt

def read_json_files(directory):
    data = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.json'):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r') as json_file:
                data.append(json.load(json_file))
    return data


def plot_volume_vs_date(data):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df['volume'] = pd.to_numeric(df['volume'])
    
    plt.figure(figsize=(20, 6))
    plt.plot(df['date'], df['volume'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.title('Stock Volume vs Date')
    plt.xticks(rotation=45)  
    plt.tight_layout()
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    json_directory = 'json_files'
    stock_data = read_json_files(json_directory)
    plot_volume_vs_date(stock_data)
