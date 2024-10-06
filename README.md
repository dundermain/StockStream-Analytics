# StockStream-Analytics
Stock Market simulation and data handling using Apache Kafka



You must have Kafka installed in your environment. 

Start the zookeper and kafka server with these commands:
1. bin/zookeeper-server-start.sh config/zookeeper.properties
2. bin/kafka-server-start.sh config/server.properties



Zookeeper helps Kafka in managing the brokers in the Kafka clusters
It notifies all nodes when the topology of the Kafka cluster changes. E.g. when brokers and topics are added or removed or when a broker goes down or comes back to running state.

ZooKeeper also controls Leader/Follower selection among multiple brokers. When a leader fails, another broker from followers takes charge as leader.


