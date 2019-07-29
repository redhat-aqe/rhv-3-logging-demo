import logging
import os
import sys

from kafka_logger.handlers import KafkaLoggingHandler


def setup_logger():
    logger = logging.getLogger("demo-app")
    logger.propagate = False
    log_level = logging.DEBUG

    log_format = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        '%Y-%m-%dT%H:%M:%S')

    # create handler to show logs at stdout
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(log_level)
    stdout_handler.setFormatter(log_format)
    logger.addHandler(stdout_handler)

    # verify that Kafka configuration is availables
    assert all([
        (key in os.environ)
        for key in ['KAFKA_SERVER', 'KAFKA_TOPIC', 'KAFKA_CERT']
    ])
    # create Kafka logging handler
    kafka_handler = KafkaLoggingHandler(
        os.environ['KAFKA_SERVER'],
        os.environ['KAFKA_TOPIC'],
        security_protocol='SSL',
        ssl_cafile=os.environ['KAFKA_CERT'],
        unhandled_exception_logger=logger,
        additional_fields={
            "service": "demo-app"
        }
    )
    kafka_handler.setFormatter(log_format)
    logger.addHandler(kafka_handler)

    logger.setLevel(log_level)
