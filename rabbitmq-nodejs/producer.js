const amqp = require('amqplib');

async function main() {
    const connection = await amqp.connect('amqp://localhost');
    const channel = await connection.createChannel();

    const queueName = 'hola';
    const message = 'Mensaje de Javascript';

    await channel.assertQueue(queueName, { durable: true });
    await channel.sendToQueue(queueName, Buffer.from(message), { persistent: true });

    console.log([x] Sent '${message}');

    await channel.close();
    await connection.close();
}

main().catch(console.error);
