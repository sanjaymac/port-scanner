import socket
from concurrent.futures import ThreadPoolExecutor

# Function to scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return f"Port {port} is open on {ip}"
        sock.close()
    except socket.error as err:
        return f"Error: {err}"
    return None

# Function to scan a range of ports on a given IP
def scan_ports(ip, start_port, end_port):
    results = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            result = future.result()
            if result:
                results.append(result)
    return results

# Main function to get input and start scanning
def main():
    ip = input("Enter IP address to scan: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"Scanning ports {start_port} to {end_port} on {ip}...")
    
    results = scan_ports(ip, start_port, end_port)
    
    if results:
        print("\n".join(results))
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
