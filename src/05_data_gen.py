from confluent_kafka import Producer
import json

# Define the Kafka configuration
conf = {'bootstrap.servers': 'localhost:29092'}

# Create a Kafka producer
producer = Producer(conf)

# Define the JSON data
data = {
    "level1": {
        "info1": "Data for level 1",
        "level2": {
            "info2": "Data for level 2",
            "level3": {
                "info3": "Data for level 3",
                "level4": [
                    {
                        "name": "John",
                        "age": 30,
                        "city": "New York",
                        "hobbies": ["reading", "swimming"],
                        "job": {
                            "title": "Engineer",
                            "company": "ABC Corp"
                        }
                    },
                    {
                        "name": "Jane",
                        "age": 25,
                        "city": "Chicago",
                        "hobbies": ["painting", "hiking"],
                        "job": {
                            "title": "Designer",
                            "company": "XYZ Corp"
                        }
                    }
                ]
            }
        }
    }
}

# Produce 100 messages to the Kafka topic
for _ in range(100):
    producer.produce('json.topic.v1', json.dumps(data))

# Wait for any outstanding messages to be delivered and delivery reports to be received
producer.flush()
