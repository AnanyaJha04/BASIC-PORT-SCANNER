import socket

def scan_port(ip_address, port):
    """Scans a single port on a given IP address."""
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(1)
        # Attempt to connect to the IP address and port
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except socket.error as e:
        print(f"Error connecting to {ip_address}:{port} - {e}")

def port_scanner(ip_address, port_list):
    """Scans a list of ports on a given IP address."""
    print(f"Scanning ports on {ip_address}...")
    for port in port_list:
        scan_port(ip_address, port)
    print("Scanning complete.")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    ports_to_scan_str = input("Enter the ports to scan (comma-separated, e.g., 80,443,22): ")
    ports_to_scan = [int(port.strip()) for port in ports_to_scan_str.split(',')]

    port_scanner(target_ip, ports_to_scan)

    
