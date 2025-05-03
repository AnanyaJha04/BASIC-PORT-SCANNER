# BASIC-PORT-SCANNER
This is a basic port scanner that scans open TCP ports using the system's IP address.

Purpose-
This code is intended to scan for any vulnerable open ports only on systems for which I have permission. The intent is just for educational purposes and basic network exploration.

Features-
1. Scanning the specified IP address.
2. Scanning TCP ports.
3. Reporting whether the port is open or there is an error in the connection.
4. If the ports are closed, it just shows "Scanning Completed".
5. Users can scan for multiple ports in an attempt.

Terminology-
1. Socket- This is a Python module that provides a low-level interface to the network socket APIs (Application Programming Interfaces) that are part of most modern operating systems. These APIs allow you to create and manipulate network connections.
2. Scan_Port- The primary purpose of the scan_port function is to attempt a TCP connection to a specific port on a given IP address. It then determines if the connection was successful, indicating that the port is likely open and listening for connections.
3. Port- A network port is a virtual endpoint (numbered 0-65535) used by network protocols like TCP and UDP to identify specific applications or services running on a device (identified by its IP address).
4. TCP- The Transmission Control Protocol (TCP) is one of the core protocols of the Internet Protocol (IP) suite. It operates at the transport layer of the TCP/IP model and provides reliable, ordered, and error-checked delivery of a stream of bytes between applications running on hosts communicating via an IP network.
5. IP address- An IP address (Internet Protocol address) is a numerical label assigned to each device (e.g., computer, smartphone, printer, server) connected to a computer network that uses the Internet Protocol for communication. It serves two main purposes: Identification and Location Addressing.

Limitations-
1. TCP Only: It only scans TCP ports, not UDP.
2. Slow: It scans ports one by one.
3. Basic Errors: It doesn't give detailed reasons for connection failures.
4. No Closed Port Reporting: It doesn't explicitly say if a port is closed.
5. No Service Info: It doesn't identify the software running on open ports.
6. Fixed Timeout: It uses a single timeout for all scans.
7. Full Connections: It establishes full TCP connections, which can be more easily detected.
8. No Hostname Handling: It might fail if you give it a website name.
9. No Rate Control: It could potentially overwhelm the target.
10. Simple Output: It just prints basic text.

Ethical Considerations-
"This script is intended for educational purposes and for scanning systems that you have explicit permission to test. Scanning networks or systems without authorization is illegal and unethical. The author is not responsible for any misuse of this tool."




