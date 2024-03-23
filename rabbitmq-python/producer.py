import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

queue_name = 'MENSAJE DE PYTHON'
message = 'HOLA JAVASCRIPT DESDE PYTHON!'

channel.queue_declare(queue=queue_name, durable=True)  # Establece durable en True
channel.basic_publish(exchange='', routing_key=queue_name, body=message, properties=pika.BasicProperties(delivery_mode=2))  # Establece delivery_mode en 2

print(f"[x] Sent '{message}'")

connection.close()
