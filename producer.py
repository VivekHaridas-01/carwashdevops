from confluent_kafka import Producer
from confluent_kafka import KafkaError
import logging as logger
from time import sleep
import json

class LogSendException(Exception):
    pass

# Kafka Producer
class kafkaProducer:
    broker = "localhost:9092"
    topic = "TestTopic"
    producer = None

    def delivery_report(self,err, msg):
        if err:
            if str(type(err).__name__) == "KafkaError":
                print(f"Message failed with error : {str(err)}")
                print(f"Message Retry? :: {err.retriable()}")
            else:
                print(f"Message failed with error : {str(err)}")
        else:
            print(f"Message delivered to partition {msg.partition()}; Offset Value - {msg.offset()}")
            print(f"{msg.value()}")

    def __init__(self):
        mylogger = logger.getLogger()
        mylogger.addHandler(logger.StreamHandler())
        try:
            self.producer = Producer({
                'bootstrap.servers': self.broker,
                'socket.timeout.ms': 100,
                'api.version.request': 'false',
                'broker.version.fallback': '0.9.0',
            },logger=mylogger
            )
        except KafkaError as exc:
            print("kafka producer - Exception during connecting to broker - {}".format(exc))

    def send_msg_async(self, msg):
        try:
            print("Send message asynchronously")
            msg = json.dumps(msg)
            self.producer.produce(self.topic,msg.encode('ascii'),callback=lambda err, original_msg=msg: self.delivery_report(err, original_msg),)    
        except KafkaError._MSG_TIMED_OUT as kte:
            logger.exception("KafkaLogsProducer timeout sending log to Kafka: %s", kte)
            raise LogSendException("KafkaLogsProducer timeout sending log to Kafka: %s" % kte)
        except KafkaError as ke:
            logger.exception("KafkaLogsProducer error sending log to Kafka: %s", ke)
            raise LogSendException("KafkaLogsProducer error sending log to Kafka: %s" % ke)
        except Exception as e:
            logger.exception("KafkaLogsProducer exception sending log to Kafka: %s", e)
            raise LogSendException("KafkaLogsProducer exception sending log to Kafka: %s" % e)
        except BufferError as buffer_error:
            print(f"{buffer_error} :: Waiting until Queue gets some free space")
            sleep(5)
        self.producer.flush()
