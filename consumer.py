from confluent_kafka import Consumer
import json
import requests
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="CarWashLog"
)

mycursor = mydb.cursor()
sql = "INSERT INTO topicdetails (module_no, place, callbackurl, time_stamp) VALUES (%s, %s, %s, %s)"


class kafkaConsumer:
    broker = "localhost:9092"
    topic = "TestTopic"
    group_id = "consumer-1"

    def start_listener(self):
        consumer_config = {
            'bootstrap.servers': self.broker,
            'group.id': self.group_id,
            'auto.offset.reset': 'earliest',
            'enable.auto.commit': 'true',
            'max.poll.interval.ms': '86400000'
        }

        consumer = Consumer(consumer_config)
        consumer.subscribe([self.topic])

        try:
            print("Listening")
            while True:
                # read single message at a time
                msg = consumer.poll(timeout=5000)

                if msg is None:
                    continue
                if msg.error():
                    print("Error reading message : {}".format(msg.error()))
                    continue
                # You can parse message and save to data base here
                d = json.loads(msg.value().decode("utf-8"))
                val = (d["Module Number"], d["Location"],
                       d["callback"], d["Date and Time"])
                mycursor.execute(sql, val)
                mydb.commit()
                URL = d["callback"]
                r = requests.get(url=URL)
                print(r.content.decode('utf-8'))
                consumer.commit()

        except Exception as ex:
            print("Kafka Exception : {}", ex)

        finally:
            print("closing consumer")
            consumer.close()


# RUNNING CONSUMER FOR READING MESSAGE FROM THE KAFKA TOPIC
my_consumer = kafkaConsumer()
my_consumer.start_listener()
