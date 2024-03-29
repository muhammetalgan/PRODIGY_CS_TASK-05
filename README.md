# Network Sniffer Tool

This Python program acts as a basic network sniffer. It listens on a specified network interface and decodes the headers of incoming IP packets, printing out some basic information.

## How it Works

The program performs network listening using Python's standard libraries, `socket` and `struct`. Additionally, third-party libraries like `pcapy` can be used to listen to network traffic on Windows operating systems.

## Usage

1. Install Python on your computer. You can download it from the [official Python website](https://www.python.org/).
2. Clone or download the code into your local machine.
3. Navigate to the directory where the program is located in your terminal or command prompt.
4. Run the program:

    ```
    python network_sniffer.py
    ```

5. The program will start listening to network traffic. It prints out the headers of each incoming IP packet.
6. To terminate the program, press `Ctrl + C`.

## Development

If you want to enhance this program or fix bugs, you can fork the code repository and make your own modifications. You can then submit a Pull Request to merge your changes into the original project.
