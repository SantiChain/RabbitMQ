import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

queue_name = 'hola'
message = 'MENSAJE DE PYTHON'

channel.queue_declare(queue=queue_name, durable=True)  # Establece durable en True
channel.basic_publish(exchange='', routing_key=queue_name, body=message, properties=pika.BasicProperties(delivery_mode=2))  # Establece delivery_mode en 2

print(f"[x] Sent '{message}'")

connection.close()
