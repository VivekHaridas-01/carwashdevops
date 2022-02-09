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

To start running your Redis server: 
`sudo service redis-server start`

Check to see if redis is working (redis-cli is the command line interface utility to talk with Redis): 
`redis-cli ping`

This should return a reply of "PONG".

To stop running your Redis server: 
`sudo service redis-server stop`
