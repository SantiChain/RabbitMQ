import pika

def callback(ch, method, properties, body):
    print(f"[x] Received {body}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

queue_name = 'hello'
channel.queue_declare(queue=queue_name, durable=True)  # Establece durable en True

print("[*] Waiting for messages. To exit, press CTRL+C")
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
