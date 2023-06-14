import socket
import threading

port_status = {
    'tcp': {
        'open': [],
        'filtered': [],
        'closed': [],
    },
    'udp': {
        'open': [],
        'filtered': [],
        'closed': [],
    }
}


def split_list_by_size(list_to_split, size):
    """
    Split a list in a list of list by a specific size
    """
    sublists = []
    sublist = []

    for item in list_to_split:
        sublist.append(item)

        if len(sublist) == size:
            sublists.append(sublist)
            sublist = []

    if sublist:
        sublists.append(sublist)

    return sublists


def check_port(host, port, protocol):
    """
    Check is the port is open, filtered or closed depending on the protocol
    """
    try:
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM if protocol == 'tcp' else socket.SOCK_DGRAM
        )
        sock.settimeout(1)

        result = sock.connect_ex((host, port))
        sock.close()
    except (socket.gaierror, Exception) as e:
        print(f'Error in port {protocol}-{port} with error: {e}')

    if result == 0:
        return 'open'
    elif result == socket.timeout:
        return 'filtered'
    return 'closed'


def worker(hostname, port, protocol):
    """
    Assign check_port result to the corresponding protocol and set the status
    """
    port_status[protocol][check_port(hostname, port, 'tcp')].append(str(port))


def run_scanner(hostname, start_port=1, end_port=1024):
    """
    Run the scanning ports in multiple threads
    """
    for protocol in ['tcp', 'udp']:
        thread_list = []

        # We split the list of ports on multiple list to avoid possible
        # concurrence problems
        all_ports = list(range(start_port, end_port + 1))
        splitted_ports = split_list_by_size(all_ports, 1024)

        for ports in splitted_ports:
            for port in ports:
                thread = threading.Thread(
                    target=worker, args=(hostname, port, protocol)
                )
                thread_list.append(thread)
                thread.start()

            for thread in thread_list:
                thread.join()


print('Port Scanner')
hostname = input(
    'Enter the target hostname or IP address (default: scanme.nmap.org): '
)
if hostname == '':
    hostname = 'scanme.nmap.org'
filename = input(
    'Enter the desired output filename (default: scan_results): '
)
if filename == '':
    filename = 'scan_results'
start_port = input('Enter the initial port number (default: 1): ')
start_port = 1 if start_port == '' else int(start_port)
if start_port < 1:
    start_port = 1
    print(
        'We have set up the start port to the lowest possible port, which is 1'
    )
end_port = input('Enter the end port number (default: 1024): ')
end_port = 1024 if end_port == '' else int(end_port)
if end_port > 65535:
    end_port = 65535
    print(
        'We have set up the end port to the biggest possible port, which is '
        '65535'
    )


run_scanner(hostname, start_port=start_port, end_port=end_port)

with open(f'{filename}.txt', 'w') as file:
    file.write('TCP Opens\n')
    file.write(', '.join(port_status['tcp']['open']))
    file.write('\n')
    file.write('TCP Filtered\n')
    file.write(', '.join(port_status['tcp']['filtered']))
    file.write('\n')
    file.write('TCP Closed\n')
    file.write(', '.join(port_status['tcp']['closed']))
    file.write('\n')
    file.write('\n')
    file.write('UDP Opens\n')
    file.write(','.join(port_status['udp']['open']))
    file.write('\n')
    file.write('UDP Filtered\n')
    file.write(','.join(port_status['udp']['filtered']))
    file.write('\n')
    file.write('UDP Closed\n')
    file.write(', '.join(port_status['udp']['closed']))

print('TCP Opens')
print(', '.join(port_status['tcp']['open']))
print('TCP Filtered')
print(', '.join(port_status['tcp']['filtered']))
# print('TCP Closed')
# print(', '.join(port_status['tcp']['closed']))
print()
print('UDP Opens')
print(', '.join(port_status['udp']['open']))
print('UDP Filtered')
print(', '.join(port_status['udp']['filtered']))
# print('UDP Closed')
# print(', '.join(port_status['udp']['closed']))
