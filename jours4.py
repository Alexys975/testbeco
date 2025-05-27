import socket
def port_scanner(target:str, start_port:int =1, end_port: int = 1024) -> None:
    print(f"Scanning target {target} from port {start_port} to {end_port}..")
    
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET FOR IPV4
        s.settimeout(0.5)  
        result = s.connect_ex((target, port))  # returns 0 if port is open

        if result == 0:
            print(f"yes// Port {port} is OPEN")
        s.close()

target_ip = input("Enter IP address or domain to scan:")
port_scanner(target_ip)

