import socket
from datetime import datetime

# Function to scan a single port
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except socket.error:
        print(f"Couldn't connect to {target}")
        return

# Main function
def run_scanner(target, port_range):
    print(f"Starting scan on {target}")
    start_time = datetime.now()
    
    for port in range(*port_range):
        scan_port(target, port)
    
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Scan completed in: {total_time}")

if __name__ == "__main__":
    # User inputs
    target = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    run_scanner(target, (start_port, end_port))
