import socket
from concurrent import futures

def check_port(target_ip, port_number, timeout, protocol):
    """
    Check is a port is open
    """
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM if protocol == 'TCP' else socket.SOCK_DGRAM
    )
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(timeout)
    try:
        sock.connect((target_ip, port_number))
        return (port_number)
    except:
        return

def port_scanner(target_ip, protocol):
    """
    Multithreading port scanning
    """
    thread_pool_size = 500
    ports_to_check = 65536

    executor = futures.ThreadPoolExecutor(max_workers=thread_pool_size)
    checks = [
        executor.submit(check_port, target_ip, port_number, 1, protocol)
        for port_number in range(0, ports_to_check, 1)
    ]

    for response in futures.as_completed(checks):
        if (response.result()):
            print(
                f'Listening on port: {response.result()} for {protocol} '
                'protocol'
            )

target_ip = '127.0.0.1'
print('What protocols will be scanned on your machine (localhost)?')
print('1) TCP (default)')
print('2) UDP')
print('3) Both')
protocol_option = input(
    'Choose an option or just press enter for the default option: '
)
print('')
protocols = {
    '1': ['TCP'],
    '2': ['UDP'],
    '3': ['TCP', 'UDP'],
}.get(protocol_option.strip(), ['TCP'])

print(f'Scanning ports for {target_ip} ...')
for protocol in protocols:
    port_scanner(target_ip, protocol)
