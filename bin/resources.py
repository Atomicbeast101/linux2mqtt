# Imports
import logging
import socket
import psutil
import config

# Attributes
logger = logging.getLogger(config.APP_NAME)
DISK_TYPES_TO_IGNORE = [
    'squashfs',
    'vfat'
]

# Functions
def get_cpu():
    AREA = 'CPU'

    try:
        data = [{
            'Utilization': {
                'name': f'{AREA} Utilization',
                'id': f'{AREA.lower()}_utilization',
                'class': None,
                'unit': '%',
                'value': psutil.cpu_percent()
            }
            # 'cores': psutil.cpu_count() # NOTE: Future expansion
        }]
        logger.debug(f'Resources output received for {AREA}: {data}')
    except psutil.AccessDenied:
        return 'ACCESS_DENIED', f'Unable to access {AREA}!'
    except psutil.TimeoutExpired:
        return 'TIMEOUT', f'Timeout when trying to retrieve {AREA}!'
    except Exception as ex:
        return 'UNKNOWN', f'Unexpected error when trying to retrieve {AREA}! Output: {str(ex)}'

    return data

def get_load_avg():
    AREA = 'Load Avg'

    try:
        output = psutil.getloadavg()
        data = [{
            '1m': {
                'name': f'{AREA} 1min',
                'id': f'{AREA.lower().replace(' ', '_')}_1minute',
                'class': None,
                'unit': None,
                'value': output[0]
            },
            '5m': {
                'name': f'{AREA} 5min',
                'id': f'{AREA.lower().replace(' ', '_')}_5minutes',
                'class': None,
                'unit': None,
                'value': output[1]
            },
            '15m': {
                'name': f'{AREA} 15min',
                'id': f'{AREA.lower().replace(' ', '_')}_15minutes',
                'class': None,
                'unit': None,
                'value': output[2]
            }
        }]
        logger.debug(f'Resources output received for {AREA}: {data}')
    except psutil.AccessDenied:
        return 'ACCESS_DENIED', f'Unable to access {AREA}!'
    except psutil.TimeoutExpired:
        return 'TIMEOUT', f'Timeout when trying to retrieve {AREA}!'
    except Exception as ex:
        return 'UNKNOWN', f'Unexpected error when trying to retrieve {AREA}! Output: {str(ex)}'

    return data

def get_ram():
    AREA = 'RAM'

    try:
        output = psutil.virtual_memory()
        data = [{
            'utilization': {
                'name': f'{AREA} Utilization',
                'id': f'{AREA.lower()}_utilization',
                'class': None,
                'unit': '%',
                'value': output.percent
            },
            'total': {
                'name': f'{AREA} Total',
                'id': f'{AREA.lower()}_total',
                'class': 'data_size',
                'unit': None,
                'value': output.total
            },
            'used': {
                'name': f'{AREA} Used',
                'id': f'{AREA.lower()}_used',
                'class': 'data_size',
                'unit': None,
                'value': output.used
            },
            'free': {
                'name': f'{AREA} Free',
                'id': f'{AREA.lower()}_free',
                'class': 'data_size',
                'unit': None,
                'value': output.free
            }
        }]
        logger.debug(f'Resources output received for {AREA}: {data}')
    except psutil.AccessDenied:
        return 'ACCESS_DENIED', f'Unable to access {AREA}!'
    except psutil.TimeoutExpired:
        return 'TIMEOUT', f'Timeout when trying to retrieve {AREA}!'
    except Exception as ex:
        return 'UNKNOWN', f'Unexpected error when trying to retrieve {AREA}! Output: {str(ex)}'

    return data

def get_swap():
    AREA = 'Swap'

    try:
        output = psutil.swap_memory()
        data = [{
            'utilization': {
                'name': f'{AREA} Utilization',
                'id': f'{AREA.lower()}_utilization',
                'class': None,
                'unit': '%',
                'value': output.percent
            },
            'total': {
                'name': f'{AREA} Total',
                'id': f'{AREA.lower()}_total',
                'class': 'data_size',
                'unit': None,
                'value': output.total
            },
            'used': {
                'name': f'{AREA} Used',
                'id': f'{AREA.lower()}_used',
                'class': 'data_size',
                'unit': None,
                'value': output.used
            },
            'free': {
                'name': f'{AREA} Free',
                'id': f'{AREA.lower()}_free',
                'class': 'data_size',
                'unit': None,
                'value': output.free
            }
        }]
        logger.debug(f'Resources output received for {AREA}: {data}')
    except psutil.AccessDenied:
        return 'ACCESS_DENIED', f'Unable to access {AREA}!'
    except psutil.TimeoutExpired:
        return 'TIMEOUT', f'Timeout when trying to retrieve {AREA}!'
    except Exception as ex:
        return 'UNKNOWN', f'Unexpected error when trying to retrieve {AREA}! Output: {str(ex)}'

    return data

def get_disks():
    AREA = 'Disk'

    try:
        data = []
        disks = psutil.disk_partitions(all=False)
        for disk in disks:
            if disk.fstype not in DISK_TYPES_TO_IGNORE:
                output = psutil.disk_usage(disk.mountpoint)
                data.append({
                    'utilization': {
                        'name': f'{AREA} {disk.mountpoint} Utilization',
                        'id': f'{AREA.lower()}_{disk.mountpoint.lower().replace('/', 'slash_').replace('__', '_')}_utilization',
                        'class': None,
                        'unit': '%',
                        'value': output.percent
                    },
                    'total': {
                        'name': f'{AREA} {disk.mountpoint} Total',
                        'id': f'{AREA.lower()}_{disk.mountpoint.lower().replace('/', 'slash_').replace('__', '_')}_total',
                        'class': 'data_size',
                        'unit': None,
                        'value': output.total
                    },
                    'used': {
                        'name': f'{AREA} {disk.mountpoint} Used',
                        'id': f'{AREA.lower()}_{disk.mountpoint.lower().replace('/', 'slash_').replace('__', '_')}_used',
                        'class': 'data_size',
                        'unit': None,
                        'value': output.used
                    },
                    'free': {
                        'name': f'{AREA} {disk.mountpoint} Free',
                        'id': f'{AREA.lower()}_{disk.mountpoint.lower().replace('/', 'slash_').replace('__', '_')}_free',
                        'class': 'data_size',
                        'unit': None,
                        'value': output.free
                    }
                })
        logger.debug(f'Resources output received for {AREA}: {data}')
    except psutil.AccessDenied:
        return 'ACCESS_DENIED', f'Unable to access {AREA}!'
    except psutil.TimeoutExpired:
        return 'TIMEOUT', f'Timeout when trying to retrieve {AREA}!'
    except Exception as ex:
        return 'UNKNOWN', f'Unexpected error when trying to retrieve {AREA}! Output: {str(ex)}'

    return data

# NOTE: Expand if needed
# def get_networks():
#     AREA = 'NETWORKS'

#     try:
#         data = {}
#         interfaces = psutil.net_io_counters(pernic=True)
#         for interface in interfaces:
#             data[interface] = {
#                 'sent': interfaces[interface].bytes_sent,
#                 'received': interfaces[interface].bytes_recv,
#                 'error_in': interfaces[interface].errin,
#                 'error_out': interfaces[interface].errout,
#                 'drop_in': interfaces[interface].dropin,
#                 'drop_out': interfaces[interface].dropout
#             }
#         print(data)
#         addresses = psutil.net_if_addrs()
#         for interface in addresses:
#             print(interface, addresses[interface])
#             data[interface]['address'] = addresses[interface][0].address
#             data[interface]['netmask'] = addresses[interface][0].netmask
#         logger.debug(f'Resources output received for {AREA}: {data}')
#     except psutil.AccessDenied:
#         return 'ACCESS_DENIED', f'Unable to access {AREA}!'
#     except psutil.TimeoutExpired:
#         return 'TIMEOUT', f'Timeout when trying to retrieve {AREA}!'
#     except Exception as ex:
#         return 'UNKNOWN', f'Unexpected error when trying to retrieve {AREA}! Output: {str(ex)}'

#     return data

# NOTE: Potential expansion for temp sensors
# psutil.sensors_temperatures()
