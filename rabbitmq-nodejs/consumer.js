const amqp = require('amqplib');

async function main() {
    const connection = await amqp.connect('amqp://localhost');
    const channel = await connection.createChannel();

    const queueName = 'hello';

    await channel.assertQueue(queueName, { durable: true }); 
    console.log('[*] Waiting for messages. To exit, press CTRL+C');

    channel.consume(queueName, (msg) => {
        console.log([x] Received ${msg.content.toString()});
    }, { noAck: true });
}

main().catch(console.error);
