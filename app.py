# Imports
from bin.log import logger
from bin import resources
from ha_mqtt_discoverable.sensors import Sensor, SensorInfo
from ha_mqtt_discoverable import Settings, DeviceInfo
import config
import time

# Attributes
SENSORS = {
    'CPU': {
        'source': resources.get_cpu,
        'sensors': {}
    },
    'LOAD_AVG': {
        'source': resources.get_load_avg,
        'sensors': {}
    },
    'RAM': {
        'source': resources.get_ram,
        'sensors': {}
    },
    'SWAP': {
        'source': resources.get_swap,
        'sensors': {}
    },
    'DISKS': {
        'source': resources.get_disks,
        'sensors': {}
    }
}

# Functions
def main():
    logger.info(f'Starting {config.APP_NAME} v{config.APP_VERSION}...')

    # Connect to MQTT server
    logger.info(f'Connecting to {config.MQTT_SERVER}:{config.MQTT_PORT} MQTT server...')
    mqtt = Settings.MQTT(
        host=config.MQTT_SERVER,
        port=config.MQTT_PORT,
        username=config.MQTT_USERNAME,
        password=config.MQTT_PASSWORD
    )
    logger.info(f'Connected to {config.MQTT_SERVER}:{config.MQTT_PORT} MQTT server!')

    # Register sensors
    logger.info(f'Registering sensors...')
    device = DeviceInfo(name=f'{config.APP_NAME}-{config.SERVER_NAME}', identifiers=f'{config.APP_NAME.lower()}_{config.SERVER_NAME.lower().replace("-", "_")}')
    for sensor in SENSORS:
        for data in SENSORS[sensor]['source']():
            for name in data:
                sensor_entity = SensorInfo(
                    name=data[name]['name'],
                    unique_id=data[name]['id'],
                    device_class=data[name]['class'],
                    unit_of_measurement=data[name]['unit'],
                    device=device
                )
                SENSORS[sensor]['sensors'][data[name]['id']] = Sensor(Settings(mqtt=mqtt, entity=sensor_entity))
    logger.info(f'Sensors registered for Home-Assistant to auto-discover!')

    logger.info(f'Started exporting sensors to MQTT...')
    while True:
        for sensor in SENSORS:
            for data in SENSORS[sensor]['source']():
                for name in data:
                    SENSORS[sensor]['sensors'][data[name]['id']].set_state(data[name]['value'])
        logger.info(f'Sensors has been updated!')
        time.sleep(config.POLLING_INTERVAL)

# Main
if __name__ == '__main__':
    main()
