import socket
import time
import random
import threading

def send_udp_packet(data, host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data.encode(), (host, port))
    sock.close()

def send_udp_packets_from_file(file_path, host, port):
    counter = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Send UDP packet
            send_udp_packet(line.strip(), host, port)
            # Introduce delay in milliseconds
            delay_in_ms = random.randrange(10, 1000)
            time.sleep(delay_in_ms / 1000.0)
            counter += 1
            print(f"Packet {counter} sent to {host}:{port} with a delay of {delay_in_ms} milliseconds")

def send_udp_packets_multithread(files_and_ports):
    threads = []
    for file_path, host, port in files_and_ports:
        thread = threading.Thread(target=send_udp_packets_from_file, args=(file_path, host, port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Specify N number of file paths and corresponding ports
    files_and_ports = [
        ('CommodityFeeds.txt', '127.0.0.1', 10023),
        # ('CommodityFeeds2.txt', '127.0.0.1', 10024),
        # Add more files and ports as needed
    ]

    # Send UDP packets from multiple files with multithreading
    send_udp_packets_multithread(files_and_ports)
