import json
from kafka import KafkaConsumer

def consume_messages(consumer, output_dir):
    for message in consumer:
        stock_data = json.loads(message.value.decode('utf-8'))
        file_name = f"{stock_data['index_name']}_{stock_data['date']}.json"
        file_path = f"{output_dir}/{file_name}"
        
        
        with open(file_path, 'w') as json_file:
            json.dump(stock_data, json_file)
        
        print(f"Saved: {file_path}")

if __name__ == "__main__":
    consumer = KafkaConsumer(
        'stock_topic',
        bootstrap_servers='localhost:9092',                            #change the ip as per your project. if you are using EC2 instance then put the ip of that
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    consume_messages(consumer, 'documents/kafka_project/json_dir')  
