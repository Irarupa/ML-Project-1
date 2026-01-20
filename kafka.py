from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'sensor-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest'
)

for message in consumer:
    print(message.value.decode())
s
