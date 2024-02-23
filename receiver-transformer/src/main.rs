use std::net::UdpSocket;
use serde_json::json;

fn main() {
    let bind_address = "127.0.0.1:10023";

    let socket = UdpSocket::bind(bind_address).expect("Failed to bind to address");

    println!("Listening for UDP packets on {}", bind_address);

    loop {
        let mut buffer = [0; 1024]; // Buffer to hold the incoming UDP packet

        let (amt, _) = socket.recv_from(&mut buffer).expect("Failed to receive data"); // Receive a UDP packet

        let received_data = String::from_utf8_lossy(&buffer[0..amt]); // Convert the received bytes to a string

		// Parse the input string and extract values
        let parts: Vec<&str> = received_data.trim().split('^').collect();
        if parts.len() == 5 {
            let commodity_name = parts[0];
            let open: i32 = parts[1].parse().expect("Failed to parse Open");
            let high: i32 = parts[2].parse().expect("Failed to parse High");
            let low: i32 = parts[3].parse().expect("Failed to parse Low");
            let close: i32 = parts[4].parse().expect("Failed to parse Close");

            // Create a JSON object
            let json_data = json!({
                "CommodityName": commodity_name,
                "Open": open,
                "High": high,
                "Low": low,
                "Close": close,
            });

            println!("{}", json_data); // Print the received JSON object

        } else {
            println!("Invalid UDP packet format");
        }
    }
}
