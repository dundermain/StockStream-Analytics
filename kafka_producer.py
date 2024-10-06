import pandas as pd
import random
import time
import json
from kafka import KafkaProducer


def load_csv_data(file_path):
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')  # Convert to list of dictionaries


def produce_messages(producer, topic, data):
    for _ in range(100):            #limiting to 100 messaged as my laptop was crashng
        random_row = random.choice(data)  
        producer.send(topic, value=random_row)
        print(f"Sent: {random_row}")
        time.sleep(1)  #sleep of 1s to prevent overload of the machine
        producer.flush()

if __name__ == "__main__":
    csv_file_path = 'stock_data.csv'  
    data = load_csv_data(csv_file_path)
    
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',           #change this to public ip if you want to stream data from your laptop on to some cloud like AWS EC2 instance. 
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    produce_messages(producer, 'stock_topic', data)
