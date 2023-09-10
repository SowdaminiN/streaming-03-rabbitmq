"""
    Sowdamini Nandigama - 09/08/2023
    This program sends a message to a queue on the RabbitMQ server.

"""

# add imports at the beginning of the file
import pika

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# use the connection to create a communication channel
ch = conn.channel()

# use the channel to declare a queue
ch.queue_declare(queue='hello')

# use the channel to publish a message to the queue
ch.basic_publish(exchange='', routing_key='hello', body='Hello World!')

# print a message to the console for the user
print(" [x] Sent 'Hello World!'")

# use the channel to declare a queue
ch.queue_declare(queue='A')

# use the channel to publish a message to the queue
ch.basic_publish(exchange='', routing_key='A', body='Hello A!')

# print a message to the console for the user
print(" [x] Sent 'Hello A!'")

# use the channel to declare a queue
ch.queue_declare(queue='B')

# use the channel to publish a message to the queue
ch.basic_publish(exchange='', routing_key='B', body='Hello B!')

# print a message to the console for the user
print(" [x] Sent 'Hello B!'")

# use the channel to declare a queue
ch.queue_declare(queue='C')

# use the channel to publish a message to the queue
ch.basic_publish(exchange='', routing_key='C', body='Hello C!')

# print a message to the console for the user
print(" [x] Sent 'Hello C!'")

# use the channel to declare a queue
ch.queue_declare(queue='D')

# use the channel to publish a message to the queue
ch.basic_publish(exchange='', routing_key='D', body='Hello D!')

# print a message to the console for the user
print(" [x] Sent 'Hello D!'")

# close the connection to the server
conn.close()
