import json
from kafka import KafkaConsumer


def create_consumer(topic_name):
    """Create and return a Kafka consumer instance."""
    return KafkaConsumer(
        topic_name,
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="user-data-consumer-group",
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )


def process_message(message):
    """Process received message."""
    # In a real application, this could include data transformation,
    # saving to database, triggering other events, etc.
    user_id = message.get("id")
    name = message.get("name")
    age = message.get("age")
    city = message.get("city")

    print(f"Processing user: {name} (ID: {user_id})")
    print(f"  Age: {age}, City: {city}")
    print("  Processing completed!")
    print("-" * 50)


def main():
    """Main function to consume messages from Kafka topic."""
    topic_name = "user-data"
    consumer = create_consumer(topic_name)

    print(f"Starting to consume messages from topic '{topic_name}'...")
    print("Waiting for messages... (Press Ctrl+C to stop)")

    try:
        for message in consumer:
            print(f"\nReceived message at offset {message.offset}:")
            user_data = message.value
            process_message(user_data)
    except KeyboardInterrupt:
        print("\nConsumer stopped by user")
    finally:
        consumer.close()
        print("Consumer closed")


if __name__ == "__main__":
    main()
