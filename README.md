# Stream-Processing-using-Kafka


This project demonstrates a simple Kafka stream processing workflow with a basic producer and consumer.

## Prerequisites

- Python 3.8+ 
- Java 8+ (required for Kafka)
- pip (Python package manager)

## Setup Instructions

### 1. Download and Setup Kafka

```bash
# Create a directory for Kafka
mkdir -p ~/kafka
cd ~/kafka

# Download Kafka 3.8.1
wget https://downloads.apache.org/kafka/3.8.1/kafka_2.13-3.8.1.tgz

# Extract the archive
tar -xzf kafka_2.13-3.8.1.tgz

# [Optional] Set up environment variables (add these to your ~/.bashrc or ~/.zshrc for permanence)
export KAFKA_HOME=~/kafka/kafka_2.13-3.8.1
export PATH=$PATH:$KAFKA_HOME/bin
```

### 2. Start Kafka Server

```bash
# Start Zookeeper (in a separate terminal)
cd ~/kafka/kafka_2.13-3.8.1
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka server (in another terminal)
cd ~/kafka/kafka_2.13-3.8.1
bin/kafka-server-start.sh config/server.properties
```

### 3. Create Kafka Topic

```bash
# Create the 'user-data' topic
cd ~/kafka/kafka_2.13-3.8.1
bin/kafka-topics.sh --create --topic user-data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### 4. Python Environment Setup

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt
```

## Running the Example

Open two terminal windows:

Terminal 1 (Consumer):
```bash
# If using a virtual environment, activate it
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

python consumer.py
```

Terminal 2 (Producer):
```bash
# If using a virtual environment, activate it
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

python producer.py
```

## Project Structure

- `data.csv`: Sample data file with user information
- `producer.py`: Kafka producer that reads from CSV and sends to Kafka topic
- `consumer.py`: Simple Kafka consumer that processes messages individually
- `requirements.txt`: Python dependencies

## What's Happening?

1. The producer reads data from the CSV file and publishes records to the 'user-data' Kafka topic
2. The consumer reads these messages and processes them one by one

## Stopping the Services

To stop Kafka and Zookeeper:

```bash
# Stop Kafka
cd ~/kafka/kafka_2.13-3.8.1
bin/kafka-server-stop.sh

# Stop Zookeeper
bin/zookeeper-server-stop.sh
```
