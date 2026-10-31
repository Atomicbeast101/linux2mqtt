# Linux2MQTT – Export System Health Metrics to MQTT for Home Assistant

Linux2MQTT is a lightweight Docker application that collects and publishes system health metrics from Windows and Linux systems using the Python `psutil` library.

Metrics are published to an MQTT broker and automatically discovered by Home Assistant through the `ha-mqtt-discoverable` library, allowing system monitoring sensors to be integrated with minimal configuration.

## Setup

Deploy the container using Docker with privileged access:

```bash
docker run -d \
  --name linux2mqtt \
  --privileged \
  --restart unless-stopped \
  -e MQTT_SERVER=localhost \
  ghcr.io/atomicbeast101/linux2mqtt:latest
```

Optionally, mount the `/logs` directory to persist application logs outside the container.

## Environment Variables

The following environment variables can be configured to customize application logging, MQTT connectivity, and metric collection intervals.

| Variable | Default | Description |
|---|---|---|
| `LOG_PATH` | `/logs` | Directory used to store application log files. |
| `LOG_LEVEL` | `INFO` | Logging verbosity level (e.g., DEBUG, INFO, WARNING, ERROR). |
| `MQTT_SERVER` | `localhost` | Hostname or IP address of the MQTT broker. |
| `MQTT_PORT` | `1883` | Port used to connect to the MQTT broker. |
| `MQTT_USERNAME` | None | Username used for MQTT broker authentication. |
| `MQTT_PASSWORD` | None | Password used for MQTT broker authentication. |
| `MQTT_TOPIC` | `homeassistant` | Base MQTT topic used to publish system metrics. |
| `POLLING_INTERVAL` | `15` | Interval, in seconds, between system metric collection cycles. |

## Sensors Exposed

The following system metrics are collected and published to MQTT:

- **CPU:** Utilization percentage
- **System Load:** Load average
- **Memory (RAM):** Utilization percentage, total, used, and available memory
- **Swap:** Utilization percentage, total, used, and free space
- **Disk:** Utilization percentage, total, used, and free space

## Software & Dependencies

- [ha-mqtt-discoverable](https://github.com/unixorn/ha-mqtt-discoverable) – Handles MQTT communication and automatic sensor discovery within Home Assistant using the Paho MQTT client.
- [psutil](https://psutil.readthedocs.io/stable/) – Cross-platform Python library for retrieving system and hardware utilization metrics.

## Documentation & AI Disclosure

AI tools were used to assist with the creation and refinement of this project's documentation. AI was not used to develop, generate, or modify the application's source code. Application development and implementation were completed independently.
