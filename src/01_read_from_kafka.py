import logging
import sys
from pyflink.common import Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaProducer, FlinkKafkaConsumer
from pyflink.datastream.formats.json import JsonRowSerializationSchema, JsonRowDeserializationSchema

def read_from_kafka(env):
  # logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=“%(message)s”)
    logger = logging.getLogger(__name__)
    try:
    # Your Flink job code here
        deserialization_schema = JsonRowDeserializationSchema.Builder() \
        .type_info(Types.ROW([Types.INT(), Types.STRING()])) \
        .build()
        
        GROUP_ID = 'GROUP_ID'
        # SASL_USERNAME = 'SASL_USERNAME' # replace with your username
        # SASL_PASSWORD = 'SASL_PASSWORD' # replace with your password
        
        TOPIC_NAME = 'json.topic.v1'
        BOOTSTRAP_SERVERS = 'localhost:29092' # 'GROUP_ID'
        properties = {
        'bootstrap.servers': BOOTSTRAP_SERVERS
        , 'group.id': GROUP_ID
        #    , 'security.protocol': 'SASL_PLAINTEXT'
        #    , 'sasl.mechanism': 'PLAIN'
        #    , 'sasl.jaas.config': 'org.apache.kafka.common.security.plain.PlainLoginModule required username=“USER” password=“PASS”;'
        }
        def process_data(data):
            # Process the data here
            return data
        kafka_consumer = FlinkKafkaConsumer(
        topics=TOPIC_NAME,
        deserialization_schema=deserialization_schema,
        properties=properties
        )
        kafka_consumer.set_start_from_earliest()
        env.add_source(kafka_consumer).map(process_data, output_type=Types.STRING())
        env.execute()
    except Exception as e:
        logger.error("Job execution failed", exc_info=True)
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")
    env = StreamExecutionEnvironment.get_execution_environment()
    # env.add_jars(“file:///C:\TEMP\_Flink\\flink-sql-connector-kafka-3.0.2-1.18.jar”)
    
    # print(“start writing data to kafka”)
    # write_to_kafka(env)
    
    print("start reading data from kafka")
    read_from_kafka(env)