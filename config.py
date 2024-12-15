from os import getenv
from dotenv import load_dotenv
import mongoengine as me
import pika


load_dotenv()
mongo_uri = getenv("MONGO_URI")
rabbitmq_uri = getenv("RABBITMQ_URI")

me.connect(
    host=mongo_uri,
    alias="default",
    )

connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_uri))
