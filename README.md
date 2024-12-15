# m8_t2

1. Clone this repository:
```bash
git clone https://github.com/Moses-93/m8_t2.git
```

2. Create the .env file in the root directory of the project:
```bash
sudo touch .env
```

3. Add your MongoDB and RabbitMQ URI to the .env file: 
```bash
MONGO_URI=mongodb://localhost:27017/email_contacts
RABBITMQ_URI=localhost
```

4. Install the required dependencies:
```bash
poetry install
```

5. Start MongoDB and RabbitMQ services:
```bash
docker compose up -d
```

6. Populate MongoDB and the RabbitMQ queue:
```bash
python producer.py
```

7. Launch the consumer to send messages:
```bash
python consumer.py
```