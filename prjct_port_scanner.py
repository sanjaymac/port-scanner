import socket
import threading

# Function to scan a single port
def scan_port(ip, port, results):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            results.append(f"Port {port} is open on {ip}")
        sock.close()
    except socket.error as err:
        results.append(f"Error: {err}")

# Function to scan a range of ports on a given IP
def scan_ports(ip, start_port, end_port, results):
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port, results))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

# Main function to get input and start scanning
def main():
    ip = input("Enter IP address to scan: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"Scanning ports {start_port} to {end_port} on {ip}...")
    
    results = []
    scan_ports(ip, start_port, end_port, results)
    
    if results:
        print("\n".join(results))
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
