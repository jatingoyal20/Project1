from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='172.16.132.160:9092')
print producer.partitions_for('foobars')
#producer.send('foobars', b'some_message_bytes'+str(0),None,0b1)

for i in range(0,10):
    producer.send('foobars', b'some_message_bytes'+str(i))