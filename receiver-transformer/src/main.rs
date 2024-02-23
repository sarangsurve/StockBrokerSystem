use std::net::UdpSocket;

fn main() {
    let bind_address = "127.0.0.1:10023";

    let socket = UdpSocket::bind(bind_address).expect("Failed to bind to address");

    println!("Listening for UDP packets on {}", bind_address);

    loop {
        let mut buffer = [0; 1024]; // Buffer to hold the incoming UDP packet

        let (data, _) = socket.recv_from(&mut buffer).expect("Failed to receive data"); // Receive a UDP packet

        let received_data = String::from_utf8_lossy(&buffer[..data]); // Convert the received bytes to a string

        println!("Received UDP packet: {}", received_data); // Print the received data
    }
}
