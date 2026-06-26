import json
import time
from kafka import KafkaProducer, KafkaConsumer

KAFKA_BROKER = "localhost:9092"
REQUEST_TOPIC = "ml-requests"
PREDICTION_TOPIC = "ml-predictions"

def run_sample_producer():
    try:
        producer = KafkaProducer(
            bootstrap_servers=[KAFKA_BROKER],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        sample_requests = [{"features": [5.1, 3.5, 1.4, 0.2]}, {"features": [7.0, 3.2, 4.7, 1.4]}]
        for req in sample_requests:
            producer.send(REQUEST_TOPIC, value=req)
        producer.flush()
        print("✅ Sample requests streamed.")
    except Exception as e:
        print(f"❌ Producer Error: {str(e)}")

if __name__ == "__main__":
    run_sample_producer()
