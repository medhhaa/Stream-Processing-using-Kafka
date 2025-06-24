import csv
import json
import time
from kafka import KafkaProducer


def create_producer():
    """Create and return a Kafka producer instance."""
    return KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
    )


def read_csv(filepath):
    """Read data from a CSV file and return a list of dictionaries."""
    data = []
    with open(filepath, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data


def main():
    """Main function to send data to Kafka topic."""
    producer = create_producer()
    data = read_csv("data.csv")

    print("Starting to send messages to Kafka topic 'user-data'...")
    for record in data:
        # Send data to Kafka topic
        producer.send("user-data", value=record)
        print(f"Sent: {record}")
        time.sleep(1)  # Send one record per second

    producer.flush()
    print("All messages sent successfully!")


if __name__ == "__main__":
    main()
