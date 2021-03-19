import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                         IPv4              TCP
# For IPv6, use AF_INET6
socket.setdefaulttimeout(1)         # Set timeout time to 1 seconds

host = input(colored("# Enter the IP address:\n=>", 'yellow'))
choice = int(input(colored("""\nWhat would you like to do:
1. Scan a specific port
2. Scan a range of ports
3. Scan first 1000 ports

->""", 'yellow')))

def portScanner(port):
    try:
        if sock.connect_ex((host, int(port))):        # If connect_ex receives an error then the port is closed.
            print(colored(f"- Port {port} is close!", 'red'))
        else:
            print(colored(f"+ Port {port} is open!", 'green'))

    except:
        print(colored("""\nERROR!\nCheck out the following things:
- The IP address should of correct format
- The port number is a correct
- Make sure you are connected to the network of the target""", 'red'))

if choice == 1:
    port = input(colored("\n# Enter the port to scan:\n=>", 'yellow'))
    portScanner(port)
elif choice == 2:
    ports = list(map(int, input(colored("\nEnter the range separated by space:\
    \n=>", 'yellow')).split()))
    for port in range(ports[0],ports[1] + 1):
        portScanner(port)
else:
    for port in range(1001):
        portScanner(port)