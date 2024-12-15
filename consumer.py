from time import sleep

import config
from models import Contact


# Функція-заглушка для надсилання email
def send_email_stub(email):
    print(f"[Consumer] Sending email to {email}...")
    sleep(2)  # Імітація затримки
    print(f"[Consumer] Email sent to {email}!")

# Обробник повідомлень
def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id).first()
    if contact and not contact.email_sent:
        send_email_stub(contact.email)
        contact.email_sent = True
        contact.save()
        print(f"[Consumer] Marked contact {contact.id} as email_sent.")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Підключення до RabbitMQ
channel = config.connection.channel()
channel.queue_declare(queue="email_queue")

print("[Consumer] Waiting for messages...")
channel.basic_consume(queue="email_queue", on_message_callback=callback)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("[Consumer] Stopping...")
    channel.stop_consuming()

config.connection.close()
