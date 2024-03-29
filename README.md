Introduction

This project aims to demonstrate the integration of Kafka messaging system with Instagram data. It provides scripts and instructions for setting up Kafka and consuming Instagram messages through Kafka producers and consumers. 
By following the provided steps, users can effectively stream Instagram messages into Kafka topics, enabling further analysis or processing downstream.



Installation


bin/zookeeper-server-start.sh config/zookeeper.properties

bin/kafka-server-start.sh config/server.properties

bin/kafka-topics.sh --create --topic instagram --bootstrap-server localhost:9092

bin/kafka-console-consumer.sh --topic instagram --bootstrap-server 172.16.231.160:9092

-------
pip install kafka-python       
----
sudo apt install docker.io

sudo docker run -it -p 8080:8080 -e DYNAMIC_CONFIG_ENABLED=true provectuslabs/kafka-ui





