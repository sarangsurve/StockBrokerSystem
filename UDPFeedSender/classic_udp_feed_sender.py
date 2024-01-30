import socket
import time
import random

def send_udp_packet(data, host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data.encode(), (host, port))
    sock.close()

def send_udp_packets_from_file(file_path, host, port):
    counter = 0
    while(True):
        with open(file_path, 'r') as file:
            for line in file:
                # Send UDP packet
                send_udp_packet(line.strip(), host, port)
                # Introduce delay in milliseconds
                delay_in_ms = random.randrange(10, 1000)
                time.sleep(delay_in_ms / 1000.0)
                counter+=1
                print("Packet "+str(counter)+" sent with delay of "+str(delay_in_ms)+" milliseconds")

if __name__ == "__main__":
    # Get environment variables or use default values
    file_path = 'CommodityFeeds.txt'
    udp_host = '127.0.0.1'
    udp_port = 10023
    # Send UDP packets from the file with the specified delay
    send_udp_packets_from_file(file_path, udp_host, udp_port)
