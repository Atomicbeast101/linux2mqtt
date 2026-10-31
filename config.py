# Imports
import socket
import os

# Config Attributes
## General
APP_NAME = 'linux2mqtt'
APP_VERSION = os.environ.get('APP_VERSION', '0.0')
SERVER_NAME = os.environ.get('SERVER_NAME', socket.gethostname())
## Logging
LOG_PATH = os.environ.get('LOG_PATH', '/logs')
LOG_RETENTION_DAYS = 10
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
## MQTT Server
MQTT_SERVER = os.environ.get('MQTT_SERVER', 'localhost')
MQTT_PORT = os.environ.get('MQTT_PORT', 1883)
MQTT_USERNAME = os.environ.get('MQTT_USERNAME', None)
MQTT_PASSWORD = os.environ.get('MQTT_PASSWORD', None)
MQTT_TOPIC = os.environ.get('MQTT_TOPIC', 'homeassistant')
## Polling
POLLING_INTERVAL = os.environ.get('POLLING_INTERVAL', 15) # In seconds
