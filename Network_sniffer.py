import socket
import struct

# Ağ arayüzünü ve boyutunu belirleyin
HOST = socket.gethostbyname(socket.gethostname())
BUFFER_SIZE = 65536

# Soketi oluşturun
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

try:
    while True:
        # Veriyi al
        packet = s.recvfrom(BUFFER_SIZE)
        packet = packet[0]

        # IP başlığını al
        ip_header = packet[0:20]
        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        iph_length = ihl * 4

        ttl = iph[5]
        protocol = iph[6]
        src_ip = socket.inet_ntoa(iph[8])
        dst_ip = socket.inet_ntoa(iph[9])

        print('IP Header:')
        print('Version:', version)
        print('IP Header Length:', ihl)
        print('TTL:', ttl)
        print('Protocol:', protocol)
        print('Source IP:', src_ip)
        print('Destination IP:', dst_ip)
        print()

except KeyboardInterrupt:
    # Program kapatılınca temizlik yap
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
