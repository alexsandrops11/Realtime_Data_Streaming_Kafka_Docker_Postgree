# Realtime_Data_Streaming_Kafka_Docker_Postgree
Data engineer project of Realtime Data Streaming using Kafka with Zookeeper, Docker, Postgree, Cassandra and Airflow 

 a real-time data streaming pipeline, covering each phase from data ingestion to processing and finally storage. We'll utilize a powerful stack of tools and technologies, including Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra—all neatly containerized using Docker.

 Data Engineering, Apache Airflow, Kafka, Apache Spark, Cassandra, PostgreSQL, Zookeeper, Docker, Docker Compose, ETL Pipeline, Data Pipeline, Big Data, Streaming Data, Real-time Analytics, Kafka Connect, Spark Master, Spark Worker, Schema Registry, Control Center, Data Streaming


# How it works
 - Airflow runing on PostgreeSQL will fetch data from open API. https://randomuser.me/
 - This data got by the API will be streaming to KAFKA which is sitting on Apache Zookeeper which is the manager all mutiple brockers that we have on Kafka. Data inside Kafka will be seen in Control Center as a UI (can see the n) and Schema Registry it provides us a seven layer for the metadata.
 - When the data will streamed to Apache Spark cluster job (by a listener), the master will decides which of the workers takes up.
 - When the taks if done will be streamed up to Cassandra (by listener)
