from kafka import KafkaConsumer

consumer = KafkaConsumer('foobars',group_id='my-groups')

print consumer.partitions_for_topic('foobars')
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print message
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))

