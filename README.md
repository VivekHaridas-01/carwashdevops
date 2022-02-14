# carwashdevops
CarWashDevOps

## Geting Started with Kafka on Windows Terminal

- Run Zookeeper: `.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties`
- Run Kafka: `.\bin\windows\kafka-server-start.bat .\config/server.properties`
- Create Topics: `.\bin\windows\kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic TestTopic`
- Delete Topics: `.\bin\windows\kafka-topics.bat --zookeeper localhost:2181 --delete --topic TestTopic`
- Show Topics List: `.\bin\windows\kafka-topics.bat --list --zookeeper localhost:2181`
- Enter Details in Topic: `.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic TestTopic`
- See details entered in Topic: `.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic TestTopic --from-beginning`
- Show Key value pairs in the Topic: `.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic TestTopic --property print.key=true --property key.separator="-" --from-beginning`
- Alter Retention Time for particular topic: `.\bin\windows\kafka-configs.bat --zookeeper localhost:2181 --alter --entity-type topics --entity-name TestTopic --add-config retention.ms=120`


## Redis Installation on WSL

1. Open your WSL terminal (ie. Ubuntu).
2. Update your Ubuntu packages: `sudo apt update` `sudo apt upgrade`
3. Once the packages have updated, install Redis with: `sudo apt install redis-server`
4. Confirm installation and get the version number: `redis-server --version`

## Getting Started with Redis on WSL

- To start running your Redis server: `sudo service redis-server start`
- Check to see if redis is working (This should return a reply of "PONG".): `redis-cli ping`
- To stop running your Redis server: `sudo service redis-server stop`
- Restart redis from wsl: `sudo service redis-server restart`
- Set password for Redis instance
  - Open terminal and connect redis-cli: `redis-cli`
  - Set passphrase: `CONFIG SET requirepass "password"`
- Authenticate your instance: auth password
- Get All Keys: KEYS *

#### A Sample Test Program for Redis `redis_test.py`
```
import redis

# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = "password"


def hello_redis():
    """Example Hello Redis Program"""
   
    # step 3: create the Redis Connection object
    try:
   
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
   
        # step 4: Set the hello message in Redis
        r.set("msg:hello", "Hello Redis!!!")

        # step 5: Retrieve the hello message from Redis
        msg = r.get("msg:hello")
        print(msg)        
   
    except Exception as e:
        print(e)


if __name__ == '__main__':
    hello_redis()
```
Run the file using `py .\redis_test.py`. You'll get the ouput: "Hello Redis!!!"


