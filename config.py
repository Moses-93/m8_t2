from os import getenv
from dotenv import load_dotenv
import mongoengine as me


load_dotenv()
mongo_uri = getenv("MONGO_URI")
rabbitmq_uri = getenv("RABBITMQ_URI")

me.connect(
    host=mongo_uri,
    alias="default",
    )
