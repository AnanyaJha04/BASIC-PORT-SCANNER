import socket

def udp_scan_port(ip_address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(0.5)
        sock.sendto(b'', (ip_address, port))
        try:
            data, addr = sock.recvfrom(1024)
            print(f"Port {port}/udp is open (response)")
        except socket.timeout:
            print(f"Port {port}/udp might be open/filtered (no response)")
        except socket.error:
            pass  
        finally:
            sock.close()
    except socket.error as e:
        print(f"Error sending to {ip_address}:{port}/udp - {e}")

def udp_port_scanner(ip_address, port_list):
   
    print(f"Scanning UDP ports on {ip_address}...")
    for port in port_list:
        udp_scan_port(ip_address, port)
    print("UDP scanning complete.")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    ports_to_scan_str = input("Enter the UDP ports to scan (comma-separated, e.g., 161,53): ")
    ports_to_scan = [int(port.strip()) for port in ports_to_scan_str.split(',')]
    udp_port_scanner(target_ip, ports_to_scan)
