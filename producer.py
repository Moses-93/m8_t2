from faker import Faker

from models import Contact
import config


# Функція для створення контактів
def generate_contacts(count):
    fake = Faker()
    contacts = []
    for _ in range(count):
        contact = Contact(
            full_name=fake.name(),
            email=fake.email()
        )
        contact.save()
        contacts.append(contact)
    return contacts

# Підключення до RabbitMQ
channel = config.connection.channel()
channel.queue_declare(queue="email_queue")

# Генеруємо контакти
contacts = generate_contacts(10)

# Додаємо контакти до черги
for contact in contacts:
    channel.basic_publish(
        exchange="",
        routing_key="email_queue",
        body=str(contact.id)
    )
    print(f"[Producer] Added contact {contact.id} to queue.")

config.connection.close()
