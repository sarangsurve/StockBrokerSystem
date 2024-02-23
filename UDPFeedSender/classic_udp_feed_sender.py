import socket
import time
import random

def send_udp_packet(data, host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data.encode(), (host, port))
    sock.close()

def generate_ohlc_candles():
    commodity_names = [{"Name": "Cotton", "Open": 60273, "High": 60780, "Low": 59940},
                        {"Name": "Bajra", "Open": 2273, "High": 2445, "Low": 1847},
                        {"Name": "Turmeric", "Open": 15453, "High": 15970, "Low": 15190},
                        {"Name": "Jeera", "Open": 26044, "High": 26390, "Low": 25800},
                        {"Name": "Steel", "Open": 42536, "High": 42620, "Low": 42500},
                        {"Name": "Chana", "Open": 5055, "High": 5212, "Low": 4943}]
    commodity_packet = commodity_names[random.randrange(0, len(commodity_names))]
    return str(commodity_packet['Name'])+"^"+str(commodity_packet['Open'])+"^"+str(commodity_packet['High'])+"^"+str(commodity_packet['Low'])+"^"+str(random.randrange(commodity_packet['Low'], commodity_packet['High']))

def send_udp_packets_from_file(host, port):
    counter = 0
    while (True):
        candle = generate_ohlc_candles()
        # Send UDP packet
        send_udp_packet(candle.strip(), host, port)
        # Introduce delay in milliseconds
        delay_in_ms = random.randrange(10, 1000)
        time.sleep(delay_in_ms / 1000.0)
        counter += 1
        print("Packet "+str(counter)+" sent with delay of " + str(delay_in_ms)+" milliseconds")

if __name__ == "__main__":
    # Get environment variables or use default values
    udp_host = '127.0.0.1'
    udp_port = 10023
    # Send UDP packets from the file with the specified delay
    send_udp_packets_from_file(udp_host, udp_port)
