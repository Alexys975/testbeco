import socket
import pyfiglet
import logging



#Configurelogginn
logging.basicConfig(filename='scan_results.log', level=logging.INFO,
                    format ='%(asctime)s - %(levelname)s - %(message)s')

ascii_banner = pyfiglet.figlet_format("P O R T /// S C A N ")
print(ascii_banner)


def port_scanner(target:str, start_port:int =1, end_port: int = 65535+1) -> None:
    print(f"Scanning target {target} from port {start_port} to {end_port}..")
    
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET FOR IPV4
        s.settimeout(0.1)  
        result = s.connect_ex((target, port))  # returns 0 if port is open

        if result == 0:
            print(f"yes// Port {port} is OPEN")             #sudo ncat -nlp "ports you want to open on Vbox (debian)"
            logging.info(f"Open port found: {target}:{port}")
        s.close()

try:
    
    target_ip = input("Enter IP address or domain name to scan:")
    ip_domain=socket.gethostbyname(target_ip)
    port_scanner(ip_domain,1,500)
    print("fin du scan")

except Exception as i:
    print(f"{i}   An ip address is composed of four numbers from 0 to 255 and separeted by dots  ")