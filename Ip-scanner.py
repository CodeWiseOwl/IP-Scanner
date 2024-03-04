import socket

# Default list of commonly used ports
DEFAULT_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 587, 993, 995]

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            pass
    return open_ports

def main():
    ip_address = input("Enter the IP address to scan: ")
    open_ports = scan_ports(ip_address, DEFAULT_PORTS)
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
